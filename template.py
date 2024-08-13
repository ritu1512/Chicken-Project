import os
from pathlib import Path

# logging is importnat for noted the log
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name= "ChickenClassifier"

# this is list we craete list of files
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requiremnets.txt",
    "setup.py",
    "research/trial.ipynb",
    "templates/index.html"



]

for filepath in list_of_files:
    filepath= Path(filepath)

    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory;  {filedir} for th efile: { filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"creating empty file: {filepath}")

    else:
        logging.info(f"craeting  {filename} is already exist")
