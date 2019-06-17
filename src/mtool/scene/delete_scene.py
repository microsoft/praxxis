"""
This file deletes the specified scene
"""

def delete_scene(args, root, history_db):
    """Deletes a scene"""
    import shutil
    import os

    from src.mtool.scene import current_scene
    from src.mtool.util import sqlite_util
    from src.mtool.cli import display
    from src.mtool.scene import scene

    if hasattr(args, "name"):
        name = args.name
    else:
        name = args

    tmp_name = scene.get_scene_by_ordinal(args, name, history_db)
    if tmp_name != None:
        name = tmp_name

    directory = os.path.join(root, name)

    if os.path.exists(directory):
        if sqlite_util.delete_scene(history_db, name):
            shutil.rmtree(directory)
            display.display_delete_scene_success(name)
        else:
            display.last_active_scene_error(name)
    else:
        display.scene_does_not_exist_error(name)
    

            
