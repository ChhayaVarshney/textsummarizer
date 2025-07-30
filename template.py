import os
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

project_name = "text_summarizer"

list_of_files = [
    ".github/.gitkeep",
    f"src/__init__.py",
    f"src/components/__init__.py",
    f"src/pipeline/__init__.py",
    f"src/utils.py",
    f"src/logger.py",
    f"src/configuration.py",
    f"src/entity.py",
    "config.yaml",
    "params.yaml",
    "app.py",
    "requirements.txt",
    "Dockerfile",
    "setup.py",
    "research/trials.ipynb",
    "main.py"
]

for filepath in list_of_files:
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info("Creating directory: {filedir} for the file {filenqame}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as file:
            pass
            logging.info("Creating empty file: {filepath}")

    else:
        logging.info("{filename} already exists.")
    
