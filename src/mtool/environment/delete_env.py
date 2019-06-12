"""
This file calls the function to delete an environment variable.

Dependencies within mtool: mtool/mtool.py
"""

import os

def delete_env(args, root):
    from src.mtool.util import sqlite_util

    current_scene = os.path.join(root, "current_scene.db")
    scene = sqlite_util.get_current_scene(current_scene)

    directory = os.path.join(root, scene)
    db_file = os.path.join(directory, f"{scene}.db")

    sqlite_util.delete_env(db_file, args.name)

