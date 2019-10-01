"""
This file ends the specified scene
"""


def end_scene(args, scene_root, history_db, current_scene_db):
    """ends a scene"""
    from src.praxxis.sqlite import sqlite_scene
    from src.praxxis.display import display_scene
    from src.praxxis.scene import scene
    from src.praxxis.util import error
    
    if hasattr(args, "name"):
        # end scene can have 0 args and end the current scene
        if(args.name is None):
            name = sqlite_scene.get_current_scene(history_db)
        else:
            name = args.name
    else:
        name = args

    try:
        tmp_name = scene.get_scene_by_ordinal(args, name, history_db)
    except error.SceneNotFoundError as e:
        raise (e)

    if tmp_name is not None:
        name = tmp_name

    try:
        sqlite_scene.mark_ended_scene(history_db, name)
    except error.SceneNotFoundError as e:
        raise e
    except error.LastActiveSceneError as e:
        raise e
    else:
        sqlite_scene.end_scene(current_scene_db, name)
        display_scene.display_end_scene_success(name)
        return(name)
