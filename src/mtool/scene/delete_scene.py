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
    from src.mtool.scene import scene

    if hasattr(args, "name"):
        if(args.name == None):
            name = sqlite_scene.get_current_scene(history_db)
        else:
            name = args.name
    else:
        name = args


    tmp_name = scene.get_scene_by_ordinal(args, name, history_db)
    if tmp_name != None:
        name = tmp_name

    directory = os.path.join(scene_root, name)

    if os.path.exists(directory):
        if sqlite_scene.delete_scene(history_db, name):
            shutil.rmtree(directory)
            display_scene.display_delete_scene_success(name)
        else:
            display_error.last_active_scene_error(name)
    else:
        display_error.scene_does_not_exist_error(name)
    

            
