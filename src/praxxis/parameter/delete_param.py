"""
This file deletes a specified parameter variable
"""


def delete_parameter(args, scene_root, history_db, current_scene_db):
    """deletes the parameter variable specified in args. Can be passed only a name or an ordinal"""
    from src.praxxis.sqlite import sqlite_parameter
    from src.praxxis.display import display_param
    from src.praxxis.util import error
    from colorama import init, Fore, Style
    init(autoreset=True)

    if hasattr(args, "name"):
        name = args.name
    else:
        name = args
        
    if str(name).isdigit():
        # checking if the user passed an ordinal instead of a string
        try:
            name = sqlite_parameter.get_param_by_ord(current_scene_db, int(name))
        except error.ParamNotFoundError as e:
            raise e
    try: 
        sqlite_parameter.delete_param(current_scene_db, name)
        return name
    except error.ParamNotFoundError as e:
        raise e
