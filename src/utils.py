import os
import yaml
from src.logger import logging
from box import ConfigBox


def read_yaml(yaml_path) -> ConfigBox:
    try:
        with open(yaml_path) as file:
            content = yaml.safe_load(file)
            logging.info(f"yaml file {yaml_path} loaded successfully.")

            return ConfigBox(content)

    except Exception as e:
        raise e


def create_directories(file_paths: list, verbose=True):
    for path in file_paths:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logging.info(f"Created directory at : {path}")
            

def get_size(path) ->str:
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f" ~ {size_in_kb} KB"

