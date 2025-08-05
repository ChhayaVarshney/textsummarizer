from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    root_dir : str
    source_url : str
    local_data_file : str
    unzip_dir : str

@dataclass
class DataValidationConfig:
    root_dir : str
    STATUS_FILE : str
    ALL_REQUIRED_FILES : list

@dataclass
class DataTransformationConfig:
    root_dir : str
    data_path : str
    tokenizer_name : str

@dataclass
class ModelTrainerConfig:
    root_dir : str
    data_path : str
    model_ckpt : str