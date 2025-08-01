from src.utils import read_yaml, create_directories
from src.logger import logging
from src.entity import DataIngestionConfig


class ConfigurationManager:
    def __init__(self):
        self.config = read_yaml("config.yaml")

        create_directories([self.config.artifacts_root])
        logging.info(f"Artifacts root directory created: {self.config.artifacts_root}")

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_url = config.source_url,
            local_data_file = config.local_data_file,
            unzip_dir = config.unzip_dir
        )
        return data_ingestion_config

