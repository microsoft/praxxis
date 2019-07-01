"""This file contains scene utilities, like initializing scenes and getting by ord"""

def get_scene_by_ordinal(args, name, history_db):
    """gets scene by ordinal using the sqlite history db"""
    from src.mtool.util.sqlite import sqlite_scene
    
    if f"{name}".isdigit():
        name = sqlite_scene.get_scene_by_ord(history_db, int(name))
        if name == "":
            from src.mtool.display import display_error
            display_error.scene_does_not_exist_error(args.name)
            return ""
        return(name)


def init_scene(scene_db, history_db, name):
    from src.mtool.util.sqlite import sqlite_scene
    sqlite_scene.init_scene(scene_db, name)
    sqlite_scene.update_current_scene(history_db, name)
