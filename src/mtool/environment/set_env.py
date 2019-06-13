"""
This file calls the function to set an environment variable for the current
    scence (a value passed on the command line)

Dependencies within mtool: mtool/mtool.py
"""

import os

def set_env(args, root, history_db):
    from src.mtool.util import sqlite_util
    from src.mtool.cli import display

    scene = sqlite_util.get_current_scene(history_db)

    directory = os.path.join(root, scene)
    db_file = os.path.join(directory, f"{scene}.db")

    sqlite_util.set_env(db_file, args.name, args.value)
    display.display_set_env(args.name, args.value)
