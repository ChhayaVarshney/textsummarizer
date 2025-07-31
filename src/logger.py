import logging 
import os
import sys
from datetime import datetime

logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)

logs_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_file_path = os.path.join(logs_dir, logs_file)

logging.basicConfig(
    format = "[ %(asctime)s ] %(name)s %(module)s %(lineno)d - %(levelname)s - %(message)s",
    level = logging.INFO,
    handlers = [
        logging.FileHandler(logs_file_path),
        logging.StreamHandler(sys.stdout)
    ]
)

