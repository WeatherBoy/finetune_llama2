import pickle

import wandb
import pandas as pd
from datasets import load_dataset
from load_data_to_finetune import load_data_to_fine_tune


def load_json_to_dataframe():
    """Load the json file into a dataframe."""
    df = pd.read_json("../../data/raw/GPT4_synthetic_data5.json")

    def transform(row):
        user_text = row["documentationInstruction"]
        assistant_text = row["processedDocumentation"]
        return (
            f"<s>[INST] <</SYS>>\nGiven a puzzle-like code question, provide a well-reasoned, step-by-step Python solution.\n<</SYS>>\n\n"
            f"{user_text} [/INST] {assistant_text} </s>"
        )

    transformed_df = df.apply(transform, axis=1).to_frame(name="text")
    transformed_df.reset_index(drop=True, inplace=True)

    return df


def load_data():
    """Load the new dataset."""
    dataset = load_dataset(wandb.config.NEW_DATASET_NAME)
    return dataset


def store_dataset_locally(dataset, filename: str | None = None) -> None:
    """Store the dataset locally using pickle."""
    filename = wandb.config.NEW_DATASET_NAME_LOCAL if filename is None else filename
    with open(filename, "wb") as file:
        pickle.dump(dataset, file)


def load_dataset_from_local(filename: str | None = None):
    """Load the dataset from a local directory using pickle."""
    filename = wandb.config.NEW_DATASET_NAME_LOCAL if filename is None else filename
    with open(filename, "rb") as file:
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
    dataset_name = "../../data/processed/process_documentation30.pkl"

    dataset = load_json_to_dataframe()
    store_dataset_locally(dataset=dataset, filename=dataset_name)
    dataset = load_dataset_from_local(filename=dataset_name)

    for i in range(5):
        print(f"** Documentation Instruction ** \n{dataset.loc[i, 'documentationInstruction']}")
        print(f"** Processed Documentation ** \n{dataset.loc[i, 'processedDocumentation']}\n\n")
