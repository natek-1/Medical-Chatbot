import os
from pathlib import Path

project_name = "transformer"

list_of_files = [

    f"{project_name}/__init__.py",
    f"{project_name}/helper.py",
    f"{project_name}/prompt.py",
    "static/style.css"
    "templates/chat.html"
    "research/trials.ipynb",
    "app.py",
    "Dockerfile",
    ".dockerignore",
    "store_index.py",
    "config/model.yaml",
    "config/schema.yaml",
]



for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        print(f"file is already present at: {filepath}")