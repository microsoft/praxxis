"""
This file calls the function to create a new scene.

Dependencies within mtool: mtool/mtool.py
"""

import os
import sys

from src.mtool.cli import mtool

def new_scene(args, root):
    if hasattr(args, "name"):
        name = args.name
    else:
        name = args
        
    from src.mtool.util import sqlite_util
    name = name.lower()
    directory = os.path.join(root, name)
    if os.path.exists(directory):
        i=1
        while os.path.exists(f"{directory}-{i}"):
            i+= 1
        directory = f"{directory}-{i}"
        name = f"{name}-{i}"
    os.mkdir(directory)
    db_file = os.path.join(directory, f"{name}.db")
    
    sqlite_util.init_scene(db_file)

    return name
