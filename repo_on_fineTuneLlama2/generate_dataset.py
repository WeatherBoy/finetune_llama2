from fine_tune_llama2 import load_data_to_fine_tune, store_dataset_locally

# from fine_tune_llama2 import transform_dataset_format


def generate_dataset():
    dataset = load_data_to_fine_tune()
    # transformed_dataset = transform_dataset_format(dataset)
    print(dataset)
    store_dataset_locally(dataset)


if __name__ == "__main__":
    generate_dataset()
