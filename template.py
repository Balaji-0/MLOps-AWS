import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:') 

project_name = "titanicspaceship"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/init.py",
    f"src/{project_name}/components/init.py",
    f"src/{project_name}/utils/init.py",
    f"src/{project_name}/config/init.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/init.py",
    f"src/{project_name}/entity/init.py",
    f"src/{project_name}/constants/init.py",
    "config/config.yaml",
    "dev.yaml",
    "params.yaml",
    "torchserve",
    "requirements.txt",
    "setup.py",
    "research.ipynb"
    "template/index.html"    
    
]

#make file path code

for filepath in list_of_files:
    filepath= Path(filepath)
    filedir,filename=os.path.split(filepath)
    
    if filedir !="":
        os.makedirs(filedir,exist_ok= True)
        logging.info(f"creating directory:{filedir} for the {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)== 0):
        with open (filepath, "w") as f:
            pass
        logging.info(f"creating file with empty file:{ filepath}")
    else:
        logging.info("file already exist")
    


