from src.configuration import ConfigurationManager
from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation
from src.logger import logging

def data_ingestion_pipeline():
    """
    Runs the data ingestion steps: download and extract.
    """
    try:
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
    except Exception as e:
        logging.error(f"An error occurred during data ingestion: {e}")
        raise e

def data_validation_pipeline():
    """
    Runs the data validation steps.
    """
    try:
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_data_files()
    except Exception as e:
        logging.error(f"An error occurred during data validation: {e}")
        raise e

def run_pipeline():
    logging.info("Starting data ingestion pipeline...")
    data_ingestion_pipeline()
    logging.info("Data ingestion pipeline completed successfully.")

    logging.info("Starting data validation pipeline...")
    data_validation_pipeline()
    logging.info("Data validation pipeline completed successfully.")

if __name__ == "__main__":
    run_pipeline()

