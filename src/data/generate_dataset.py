import pickle

import hydra
import wandb
import pandas as pd
from omegaconf import DictConfig, OmegaConf


@hydra.main(config_path="../../conf", config_name="config_LoRA", version_base="1.2")
def load_configs(cfg: DictConfig):
    temp_config = OmegaConf.to_container(cfg, resolve=True, throw_on_missing=True)

    system_config = temp_config["system_parameters"]  # <-- the "|" operator merges the two dictionaries

    wandb.init(project="test 1", config=system_config)


def load_json_to_dataframe(filename: str | None = None) -> pd.DataFrame:
    """Load the json file into a dataframe."""
    if filename is None:
        filename = "../" + wandb.config.DATASET_NAME
    df = pd.read_json(filename)
    return df


def store_dataset_locally(dataset: pd.DataFrame, filename: str | None = None) -> None:
    """Store the dataset locally using pickle."""
    if filename is None:
        filename = wandb.config.NEW_DATASET_NAME_LOCAL

    with open(filename, "wb") as file:
        pickle.dump(dataset, file)


def load_dataset_from_local(filename: str | None = None) -> pd.DataFrame:
    """Load the dataset from a local directory using pickle."""
    if filename is None:
        filename = wandb.config.NEW_DATASET_NAME_LOCAL

    with open(filename, "rb") as file:
        dataset = pickle.load(file)

    return dataset


def transform_dataset_format(df: pd.DataFrame) -> pd.DataFrame:
    """Transform the dataframe into a specified format."""

    def transform(row):
        user_text = row[wandb.config.X_COLUMN]
        assistant_text = row[wandb.config.Y_COLUMN]
        return f"<s>[INST] <</SYS>>\n{wandb.config.SYSTEM_MESSAGE.strip()}\n<</SYS>>\n\n" f"{user_text} [/INST] {assistant_text} </s>"

    transformed_df = df.apply(transform, axis=1).to_frame(name="text")
    transformed_df.reset_index(drop=True, inplace=True)

    return transformed_df


if __name__ == "__main__":
    load_configs()
    dataset_name_local = "../../data/processed/" + wandb.config.NEW_DATASET_NAME_LOCAL

    dataset = load_json_to_dataframe(filename="../../data/raw/GPT4_synthetic_data.json")
    transformed_dataset = transform_dataset_format(dataset)
    store_dataset_locally(dataset=dataset, filename=dataset_name_local)
    dataset = load_dataset_from_local(filename=dataset_name_local)

    for i in range(5):
        print(f"** Documentation Instruction ** \n{dataset.loc[i, 'documentationInstruction']}")
        print(f"** Processed Documentation ** \n{dataset.loc[i, 'processedDocumentation']}\n\n")
