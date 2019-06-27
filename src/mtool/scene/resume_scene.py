"""
This file resumes a previously used scene.
"""

def resume_scene(args, scene_root, history_db):
    """Resumes a scene"""
    import os

    from src.mtool.util import sqlite_util
    from src.mtool.display import display_scene
    from src.mtool.scene import scene

    if hasattr(args, "name"):
        name = args.name
    else:
        name = args

    tmp_name = scene.get_scene_by_ordinal(args, name, history_db)
    if tmp_name != None:
        name = tmp_name

    scene = os.path.join(scene_root, name, f"{name}.db" )

    sqlite_util.resume_scene(scene, name)
    sqlite_util.mark_resumed_scene(history_db, name)
    sqlite_util.update_current_scene(history_db, name)
    
    display_scene.display_resume_scene(name)