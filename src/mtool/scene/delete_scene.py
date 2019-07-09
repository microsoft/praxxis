"""
This file deletes the specified scene
"""

def delete_scene(args, scene_root, history_db):
    """Deletes a scene"""
    import shutil
    import os

    from src.mtool.scene import current_scene
    from src.mtool.util.sqlite import sqlite_scene
    from src.mtool.display import display_scene
    from src.mtool.display import display_error
    from src.mtool.util import error
    from src.mtool.scene import scene

    if hasattr(args, "name"):
        if(args.name == None):
            name = sqlite_scene.get_current_scene(history_db)
        else:
            name = args.name
    else:
        name = args


    try:
        tmp_name = scene.get_scene_by_ordinal(args, name, history_db)
    except error.SceneNotFoundError as e:
        raise e
    except error.EndEndedSceneError as e:
        pass
        
    if tmp_name != None:
        name = tmp_name

    directory = os.path.join(scene_root, name)

    if os.path.exists(directory):
        try:
            sqlite_scene.delete_scene(history_db, name)
            shutil.rmtree(directory)
            display_scene.display_delete_scene_success(name)
            return name
        except error.LastActiveSceneError as e:
            raise e
    else:
        raise error.SceneNotFoundError(name)
    