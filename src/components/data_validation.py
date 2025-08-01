import os
from src.logger import logging
from src.entity import DataValidationConfig

class DataValidation:
    def __init__(self, config):
        self.config = config

    def validate_all_data_files(self) -> bool:
        try:
            validation_status = None

            all_files = os.listdir(os.path.join("artifacts", "samsum_dataset"))

            for file in all_files:
                if file not in self.config.ALL_REQUIRED_FILES:
                    validation_status = False
                    logging.error(f"Missing file: {file}")
                else:
                    validation_status = True
                    logging.info(f"Found required file: {file}")
                
            with open(self.config.STATUS_FILE, "w") as f:
                f.write(f"Validation status: {validation_status}")
            
            return validation_status

        except Exception as e:
            logging.error(f"Failed to validate data files: {e}")
            return False

   