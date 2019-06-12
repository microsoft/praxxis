"""
This file calls the function to delete an environment variable.

Dependencies within mtool: mtool/mtool.py
"""

import os

def delete_env(args, root, history_db):
    from src.mtool.util import sqlite_util

    scene = sqlite_util.get_current_scene(history_db)
    
    directory = os.path.join(root, scene)
    db_file = os.path.join(directory, f"{scene}.db")

    sqlite_util.delete_env(db_file, args.name)

