import hydra
from omegaconf import OmegaConf
from models.fine_tune_llama2 import fine_tune_and_save_model, initialize_model_and_tokenizer, load_data, visualize_and_save


@hydra.main(config_path="../conf", config_name="config", version_base="1.2")
def main(cfg):
    print(OmegaConf.to_yaml(cfg))


def fine_tune():
    transformed_dataset = load_data()
    model, tokenizer = initialize_model_and_tokenizer()
    _, metrics = fine_tune_and_save_model(model, tokenizer, transformed_dataset["train"], transformed_dataset["test"])
    exec_time = metrics["exec_time"]
    memory_usage = metrics["peak_mem_consumption"]
    visualize_and_save(exec_time, memory_usage)


if __name__ == "__main__":
    print("Running fine_tune.py")
    main()
