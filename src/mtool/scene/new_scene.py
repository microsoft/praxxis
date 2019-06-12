"""
This file calls the function to create a new scene.

Dependencies within mtool: mtool/mtool.py
"""

import os

def new_scene(args, root):
    from src.mtool.util import sqlite_util

    if hasattr(args, "name"):
        name = args.name
    else:
        name = args
        
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
    
    sqlite_util.init_scene(db_file, name)
    current_scene = os.path.join(root, "current_scene.db")
    sqlite_util.update_current_scene(current_scene, name)

    return name
    ##TODO: create prints to show that a scene has been created
