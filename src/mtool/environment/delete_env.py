"""
This file deletes a specified environment variable
"""

import os

def delete_env(args, root, history_db, current_scene_db):
    """deletes the environment variable specified in args. Can be passed only a name or an ordinal"""
    from src.mtool.util import sqlite_util
    from src.mtool.cli import display

    if hasattr(args, "name"):
        name = args.name
    else:
        name = args

    if f"{name}".isdigit():
        """checking if the user passed an ordinal instead of a string"""
        name = sqlite_util.get_env_by_ord(current_scene_db, int(name))
        if name == "":
            display.env_not_found_error(args.name)
            return

    if(sqlite_util.delete_env(current_scene_db, name)):
        display.display_delete_env(name)
    else:
        display.env_not_found_error(name)
    
