"""This file contains scene utilities, like initializing scenes and getting by ord"""

def get_scene_by_ordinal(args, name, history_db):
    """gets scene by ordinal using the sqlite history db"""
    from src.mtool.sqlite import sqlite_scene
    from src.mtool.util import error

    if f"{name}".isdigit():
        try:
            name = sqlite_scene.get_scene_by_ord(history_db, int(name))
        except error.SceneNotFoundError as e:
            raise e
        else:
            return(name)


def init_scene(scene_db, history_db, name):
    from src.mtool.sqlite import sqlite_scene
    sqlite_scene.init_scene(scene_db, name)
    sqlite_scene.update_current_scene(history_db, name)
    return (scene_db, name)

