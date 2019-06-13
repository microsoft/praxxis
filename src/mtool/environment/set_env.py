"""
This file calls the function to set an environment variable for the current
    scence (a value passed on the command line)

Dependencies within mtool: mtool/mtool.py
"""

import os

def set_env(args, root, history_db, current_scene_db):
    from src.mtool.util import sqlite_util
    from src.mtool.cli import display

    sqlite_util.set_env(current_scene_db, args.name, args.value)
    display.display_set_env(args.name, args.value)
