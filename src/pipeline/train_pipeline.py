from src.configuration import ConfigurationManager
from src.components.data_ingestion import DataIngestion
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

def run_pipeline():
    logging.info("Starting data ingestion pipeline...")
    data_ingestion_pipeline()
    logging.info("Data ingestion pipeline completed successfully.")

if __name__ == "__main__":
    run_pipeline()

