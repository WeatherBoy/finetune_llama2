import functools
import os
import pickle
import time

import hydra
import pandas as pd
import torch
import wandb
from datasets import Dataset, load_dataset
from omegaconf import DictConfig, OmegaConf
from peft import LoraConfig, PeftModel, get_peft_model, prepare_model_for_kbit_training
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig, EarlyStoppingCallback, TrainingArguments, pipeline
from trl import SFTTrainer


@hydra.main(config_path="../conf", config_name="config", version_base="1.2")
def main(cfg: DictConfig):
    temp_config = OmegaConf.to_container(cfg, resolve=True, throw_on_missing=True)

    config = temp_config["hyperparameters"] | temp_config["system_parameters"]  # <-- the "|" operator merges the two dictionaries

    wandb.init(project="test 1", config=config)


def time_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result, metrics = func(*args, **kwargs)
        end_time = time.time()
        exec_time = end_time - start_time
        metrics["exec_time"] = exec_time
        return result, metrics

    return wrapper


def memory_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        torch.cuda.empty_cache()
        torch.cuda.reset_peak_memory_stats()
        result, metrics = func(*args, **kwargs)
        peak_mem = torch.cuda.max_memory_allocated()
        peak_mem_consumption = peak_mem / 1e9
        metrics["peak_mem_consumption"] = peak_mem_consumption
        return result, metrics

    return wrapper


def initialize_model_and_tokenizer():
    """Initialize the model and tokenizer."""

    compute_dtype = getattr(torch, wandb.config.BNB_4BIT_COMPUTE_DTYPE)
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=wandb.config.USE_4BIT,
        bnb_4bit_quant_type=wandb.config.BNB_4BIT_COMPUTE_QUANT_TYPE,
        bnb_4bit_compute_dtype=compute_dtype,
        bnb_4bit_use_double_quant=wandb.config.USE_NESTED_QUANT,
    )
    model = AutoModelForCausalLM.from_pretrained(wandb.config.MODEL_NAME, quantization_config=bnb_config, device_map=wandb.config.DEVICE_MAP)
    model.config.use_cache = False
    model.config.pretraining_tp = 1
    tokenizer = AutoTokenizer.from_pretrained(wandb.config.MODEL_NAME, trust_remote_code=True)
    tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "right"

    return model, tokenizer


def configure_training_args():
    """Configure training arguments."""
    return TrainingArguments(
        output_dir=wandb.config.OUTPUT_DIR,
        num_train_epochs=wandb.config.NUM_EPOCHS,
        per_device_train_batch_size=wandb.config.PER_DEVICE_TRAIN_BATCH_SIZE,
        gradient_accumulation_steps=wandb.config.GRAD_ACC_STEPS,
        optim=wandb.config.OPTIM,
        save_steps=wandb.config.SAVE_STEPS,
        logging_steps=wandb.config.LOG_STEPS,
        learning_rate=wandb.config.LEARNING_RATE,
        weight_decay=wandb.config.WEIGHT_DECAY,
        fp16=wandb.config.FP16,
        bf16=wandb.config.BF16,
        max_grad_norm=wandb.config.MAX_GRAD_NORM,
        max_steps=wandb.config.MAX_STEPS,
        warmup_ratio=wandb.config.WARMUP_RATIO,
        group_by_length=wandb.config.GROUP_BY_LENGTH,
        lr_scheduler_type=wandb.config.SCHEDULER_TYPE,
        report_to="all",
        evaluation_strategy="steps",
        eval_steps=50,
        load_best_model_at_end=True,
    )


@memory_decorator
@time_decorator
def fine_tune_and_save_model(model, tokenizer, train_dataset, val_dataset):
    """Fine-tune the model and save it."""

    peft_config = LoraConfig(
        lora_alpha=wandb.config.LORA_ALPHA,
        lora_dropout=wandb.config.LORA_DROPOUT,
        r=wandb.config.LORA_R,
        bias="none",
        task_type="CAUSAL_LM",
    )

    model = prepare_model_for_kbit_training(model)
    model = get_peft_model(model, peft_config)

    model.print_trainable_parameters()

    training_args = configure_training_args()

    early_stopping = EarlyStoppingCallback(early_stopping_patience=4)

    trainer = SFTTrainer(
        model=model,
        train_dataset=train_dataset,
        eval_dataset=val_dataset,
        dataset_text_field="text",
        peft_config=peft_config,
        tokenizer=tokenizer,
        args=training_args,
        max_seq_length=512,
        callbacks=[early_stopping],
    )
    trainer.train()

    if not os.path.exists(wandb.config.NEW_MODEL_PATH):
        os.makedirs(wandb.config.NEW_MODEL_PATH)

    trainer.model.save_pretrained(wandb.config.NEW_MODEL_PATH)
    tokenizer.save_pretrained(wandb.config.NEW_MODEL_PATH)

    del model
    torch.cuda.empty_cache()

    return None, {}


def generate_code_from_prompt(model, tokenizer):
    """
    Generate code based on the provided system message using a pre-trained model and tokenizer.
    """
    prompt = f"[INST] <<SYS>>\n{wandb.config.SYSTEM_MESSAGE}\n<</SYS>>\n\n" f"Write a function that reverses a linked list. [/INST]"

    pipe = pipeline(task="text-generation", model=model, tokenizer=tokenizer, max_length=500)

    result = pipe(prompt)
    generated_text = result[0]["generated_text"]

    return generated_text


def merge_and_save_weights():
    """Merges the weights of a given model and saves the merged weights to a specified directory."""

    if not os.path.exists(wandb.config.NEW_MODEL_PATH_MERGE):
        os.makedirs(wandb.config.NEW_MODEL_PATH_MERGE)

    base_model = AutoModelForCausalLM.from_pretrained(
        wandb.config.MODEL_NAME,
        low_cpu_mem_usage=True,
        return_dict=True,
        torch_dtype=torch.float16,
        device_map=wandb.config.DEVICE_MAP,
    )
    model = PeftModel.from_pretrained(base_model, wandb.config.NEW_MODEL_NAME)
    model = model.merge_and_unload()

    tokenizer = AutoTokenizer.from_pretrained(wandb.config.MODEL_NAME, trust_remote_code=True)
    tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "right"

    model.save_pretrained(wandb.config.NEW_MODEL_PATH)
    tokenizer.save_pretrained(wandb.config.NEW_MODEL_PATH)


def publish_to_hugging_face(df, dataset_name, top=None):
    """Publish the transformed dataframe to Hugging Face datasets."""
    dataset = Dataset.from_pandas(df)

    if top is not None:
        dataset = dataset.select(range(top))
        splits = dataset.train_test_split(test_size=1000, shuffle=True)
    else:
        splits = dataset

    splits.push_to_hub(dataset_name)


def print_trainable_parameters(model):
    """Prints the number of trainable parameters in the model."""
    trainable_params = 0
    all_param = 0
    for _, param in model.named_parameters():
        all_param += param.numel()
        if param.requires_grad:
            trainable_params += param.numel()
    print(f"trainable params: {trainable_params} || " f"all params: {all_param} || " f"trainable%: {100 * trainable_params / all_param}")


def push_model_to_hub():
    """Push the fine-tuned model and tokenizer to the Hugging Face Hub."""
    model = AutoModelForCausalLM.from_pretrained(wandb.config.NEW_MODEL_PATH)
    tokenizer = AutoTokenizer.from_pretrained(wandb.config.NEW_MODEL_PATH)

    model.push_to_hub(wandb.config.HF_HUB_MODEL_NAME, use_temp_dir=False)
    tokenizer.push_to_hub(wandb.config.HF_HUB_MODEL_NAME, use_temp_dir=False)