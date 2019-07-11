"""
This file deletes a specified environment variable
"""

def delete_env(args, scene_root, history_db, current_scene_db):
    """deletes the environment variable specified in args. Can be passed only a name or an ordinal"""
    from src.mtool.util.sqlite import sqlite_environment
    from src.mtool.display import display_env
    from src.mtool.util import error
    from colorama import init, Fore, Style
    init(autoreset=True)

    if hasattr(args, "name"):
        name = args.name
    else:
        name = args
        
    if f"{name}".isdigit():
        #checking if the user passed an ordinal instead of a string
        try:
            name = sqlite_environment.get_env_by_ord(current_scene_db, int(name))
        except error.EnvNotFoundError as e:
            raise e
    try: 
        sqlite_environment.delete_env(current_scene_db, name)
        return name
    except error.EnvNotFoundError as e:
        raise e
