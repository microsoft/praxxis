"""
This file sets an parameter variable for the current
    scence (a value passed on the command line)
"""

def set_param(args, scene_root, history_db, current_scene_db):
    """sets the parameter by making a sqlite call"""
    from src.praxxis.sqlite import sqlite_parameter
    from src.praxxis.display import display_param
    from src.praxxis.util import error

    if hasattr(args, "name"):
        name = args.name
    else:
        name = args
        
    if str(name).isdigit():
        #checking if the user passed an ordinal instead of a string
        try:
            name = sqlite_parameter.get_param_by_ord(current_scene_db, int(name))
        except error.ParamNotFoundError as e:
            raise e

    sqlite_parameter.set_param(current_scene_db, name, args.value)
    display_param.display_set_param(name, args.value)
    return args
