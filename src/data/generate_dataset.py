import pickle

import wandb
from datasets import load_dataset
from fine_tune_llama2 import load_data_to_fine_tune, store_dataset_locally

# from fine_tune_llama2 import transform_dataset_format


def load_data():
    """Load the new dataset."""
    dataset = load_dataset(wandb.config.NEW_DATASET_NAME)
    return dataset


def store_dataset_locally(dataset):
    """Store the dataset locally using pickle."""
    with open(wandb.config.NEW_DATASET_NAME_LOCAL, "wb") as file:
        pickle.dump(dataset, file)


def load_dataset_from_local():
    """Load the dataset from a local directory using pickle."""
    with open(wandb.config.NEW_DATASET_NAME_LOCAL, "rb") as file:
        dataset = pickle.load(file)
    return dataset


def transform_dataset_format(df):
    """Transform the dataframe into a specified format."""

    def transform(row):
        user_text = row["question"]
        assistant_text = row["answer"]
        return f"<s>[INST] <</SYS>>\n{wandb.config.SYSTEM_MESSAGE.strip()}\n<</SYS>>\n\n" f"{user_text} [/INST] {assistant_text} </s>"

    transformed_df = df.apply(transform, axis=1).to_frame(name="text")
    transformed_df.reset_index(drop=True, inplace=True)

    return transformed_df


def generate_dataset():
    dataset = load_data_to_fine_tune()
    # transformed_dataset = transform_dataset_format(dataset)
    print(dataset)
    store_dataset_locally(dataset)


if __name__ == "__main__":
    generate_dataset()
