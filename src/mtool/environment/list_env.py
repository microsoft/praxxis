"""
This file calls the function to list all environment variables.

Dependencies within mtool: mtool/mtool.py
"""

import os

def list_env(args, root, history_db, start, end):
    from src.mtool.util import sqlite_util
    from src.mtool.cli import display
    
    scene = sqlite_util.get_current_scene(history_db)

    directory = os.path.join(root, scene)
    db_file = os.path.join(directory, f"{scene}.db")

    display.display_list_env(sqlite_util.list_env(db_file, start, end))
