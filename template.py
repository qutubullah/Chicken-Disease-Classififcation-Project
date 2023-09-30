import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')

proj_name = "cnnClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{proj_name}/__init__.py",
    f"src/{proj_name}/components/__init__.py",
    f"src/{proj_name}/utils/__init__.py",
    f"src/{proj_name}/config/__init__.py",
    f"src/{proj_name}/config/configuration.p",
    f"src/{proj_name}/pipeline/__init__.py",
    f"src/{proj_name}/entity/__init__.py",
    f"src/{proj_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.pynb"
    ]
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the {filename}")

    if not (os.path.exists(filepath)) or (os.path.getsize(filename) == 0):
        with open(filepath , "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} is already exists")