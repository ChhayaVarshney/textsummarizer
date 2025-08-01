import os
import zipfile
import urllib.request as request
from src.logger import logging
from src.configuration import ConfigurationManager

class DataIngestion:
    def __init__(self, config):
        self.config = config

    def download_file(self):
        try:
            if not os.path.exists(self.config.local_data_file):
                filename, headers = request.urlretrieve(
                    url = self.config.source_url,
                    filename = self.config.local_data_file
                )
                logging.info(f"Downloaded {filename} with folloing info: \n{headers}")
            else:    
                logging.info(f"{self.config.local_data_file} already exists, deleting and re-downloading.")
                os.remove(self.config.local_data_file)
                self.download_file()

        except Exception as e:
            logging.error(f"Failed to download file: {e}")

    def extract_zip_file(self):
        try:
            unzip_path = self.config.unzip_dir
            os.makedirs(unzip_path, exist_ok=True)
            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
                logging.info(f"Extracted files from {self.config.local_data_file} to {unzip_path}.")
        
        except Exception as e:
            logging.error(f"Failed to extract files: {e}")
            raise e

