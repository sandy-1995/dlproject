import os
from pathlib import Path
import logging

logging.basicConfig(
    level= logging.INFO,
    filename="template_structure.log",
    filemode='w',
    format= '%(asctime)s - %(message)s',
    datefmt='%d-%b-%y %H:%M:%S'
)

list_of_files = [
    "artifacts/data_set.csv",
    "notebook/project.ipynb",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/pipeline/__init__.py",
    "src/pipeline/predict_pipeline.py",
    "src/pipeline/test_pipeline.py",
    "src/__init__.py",
    "src/logger.py",
    "src/exception.py",
    "src/utils.py",
    "static/style.css",
    "template/index.html",
    "template/predict.html",
    "setup.py",
    "requirements.txt",
    "app.py",
    "Dockerfile",
    "Procfile"
]

for filepath in list_of_files:
    filepath = Path(filepath) 
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    if (not os.path.exists(filepath) or (os.path.getsize(filepath) == 0)):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")

logging.info("Project Structure is completed") 
