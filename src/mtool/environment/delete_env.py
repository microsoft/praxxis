"""
This file calls the function to delete an environment variable.

Dependencies within mtool: mtool/mtool.py
"""

import os

def delete_env(args, root, history_db, current_scene_db):
    from src.mtool.util import sqlite_util
    from src.mtool.cli import display

    if hasattr(args, "name"):
        name = args.name
    else:
        name = args

    if f"{name}".isdigit():
        name = sqlite_util.get_env_by_ord(current_scene_db, int(name))
        if name == "":
            display.env_not_found_error(args.name)
            return

    if(sqlite_util.delete_env(current_scene_db, name)):
        display.display_delete_env(name)
    else:
        display.env_not_found_error(name)
    
