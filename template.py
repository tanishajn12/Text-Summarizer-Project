import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] : %(message)s:')

project_name = "textSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/_init_.py",
    f"src/{project_name}/components/_init_.py",
    f"src/{project_name}/utils/_init_.py",
    f"src/{project_name}/utils/common.py",   
    f"src/{project_name}/logging/_init_.py", 
    f"src/{project_name}/config/configuration.py", 
    f"src/{project_name}/pipeline/_init_.py", 
    f"src/{project_name}/entity/_init_.py",
    f"src/{project_name}/constant/_init_.py",  
    "config/config.yaml"  ,
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
    
]


for filepath in list_of_files :
    filepath = Path(filepath)