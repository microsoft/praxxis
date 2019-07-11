"""
This file changes the current scene.
"""

def change_scene(args, scene_root, history_db):
    """changes current scene in sqlite history db"""
    from src.mtool.util.sqlite import sqlite_scene
    from src.mtool.display import display_scene
    from src.mtool.scene import scene
    from src.mtool.util import error

    if hasattr(args, "name"):
        name = args.name
    else:
        name = args

    try:
        tmp_name = scene.get_scene_by_ordinal(args, name, history_db)
    except error.SceneNotFoundError as e:
        raise e

    if tmp_name != None:
        name = tmp_name

    try:
        sqlite_scene.check_scene_ended(history_db, name) 
    except error.SceneNotFoundError as e:
        raise e
    except error.SceneEndedError as e:
        raise e 
    else:
        sqlite_scene.update_current_scene(history_db, name)
        display_scene.display_change_scene(name)
    return name