"""
This file resumes a previously used scene.
"""

def resume_scene(args, scene_root, history_db):
    """Resumes a scene"""
    import os

    from src.mtool.util import sqlite_util
    from src.mtool.cli import display
    from src.mtool.scene import scene

    scene.init_scene(scene_root, history_db)

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
    
    display.display_resume_scene(name)