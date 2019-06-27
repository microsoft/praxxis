"""This file contains scene utilities, like initializing scenes and getting by ord"""




def get_scene_by_ordinal(args, name, history_db):
    """gets scene by ordinal using the sqlite history db"""
    from src.mtool.util import sqlite_util
    from src.mtool.display import display_error

    if f"{name}".isdigit():
        name = sqlite_util.get_scene_by_ord(history_db, int(name))
        if name == "":
            from src.mtool.cli import display
            display_error.scene_does_not_exist_error(args.name)
            return ""
        return(name)