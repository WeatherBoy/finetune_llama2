from models.fine_tune_llama2 import fine_tune_and_save_model, initialize_model_and_tokenizer, load_data
from visualisation.visualise_llama2 import visualize_and_save


def fine_tune():
    transformed_dataset = load_data()
    model, tokenizer = initialize_model_and_tokenizer()
    _, metrics = fine_tune_and_save_model(model, tokenizer, transformed_dataset["train"], transformed_dataset["test"])
    exec_time = metrics["exec_time"]
    memory_usage = metrics["peak_mem_consumption"]
    visualize_and_save(exec_time, memory_usage)


if __name__ == "__main__":
    print("Running fine_tune.py")
    fine_tune()
