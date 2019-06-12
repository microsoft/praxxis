"""
This file calls the function to set an environment variable for the current
    scence (a value passed on the command line)

Dependencies within mtool: mtool/mtool.py
"""

import os

def set_env(args, root):
    from src.mtool.util import sqlite_util

    current_scene = os.path.join(root, "current_scene.db")
    scene = sqlite_util.get_current_scene(current_scene)

    directory = os.path.join(root, scene)
    db_file = os.path.join(directory, f"{scene}.db")

    sqlite_util.set_env(db_file, args.name, args.value)

