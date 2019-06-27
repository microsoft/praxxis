"""
This file changes the current scene.
"""

def change_scene(args, scene_root, history_db):
    """changes current scene in sqlite history db"""
    from src.mtool.util import sqlite_util
    from src.mtool.display import display_scene
    from src.mtool.display import display_error
    from src.mtool.scene import scene


    if hasattr(args, "name"):
        name = args.name
    else:
        name = args

    tmp_name = scene.get_scene_by_ordinal(args, name, history_db)
    if tmp_name != None:
        name = tmp_name

    ended = sqlite_util.check_scene_ended(history_db, name) 

    if ended == -1:
        display_error.scene_does_not_exist_error(name)
    elif ended:
        display_error.scene_ended_error(name)
    else:
        sqlite_util.update_current_scene(history_db, name)
        display_scene.display_change_scene(name)
