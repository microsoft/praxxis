"""
This file sets an environment variable for the current
    scence (a value passed on the command line)
"""

def set_env(args, scene_root, history_db, current_scene_db):
    """sets the environment by making a sqlite call"""
    from src.mtool.util.sqlite import sqlite_environment
    from src.mtool.display import display_env
    from src.mtool.display import display_error

    if hasattr(args, "name"):
        name = args.name
    else:
        name = args

    if f"{name}".isdigit():
        """checking if the user passed an ordinal instead of a string"""
        name = sqlite_environment.get_env_by_ord(current_scene_db, int(name))
        if name == "":
            display_error.env_not_found_error(args.name)
            return

    sqlite_environment.set_env(current_scene_db, name, args.value)
    display_env.display_set_env(name, args.value)
