"""
This file sets an environment variable for the current
    scence (a value passed on the command line)
"""

def set_env(args, scene_root, history_db, current_scene_db):
    """sets the environment by making a sqlite call"""
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

    sqlite_util.set_env(current_scene_db, name, args.value)
    display.display_set_env(name, args.value)
