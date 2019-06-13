"""
This file calls the function to resume a previously used scene.

Dependencies within mtool: mtool/mtool.py
"""

import os

def resume_scene(args, root, history_db):
    """Resumes a scene"""
    from src.mtool.util import sqlite_util
    from src.mtool.cli import display
    from src.mtool.scene import scene

    if hasattr(args, "name"):
        name = args.name
    else:
        name = args

    tmp_name = scene.get_scene_by_ordinal(args, name, history_db)
    if tmp_name == "":
        return
    else:
        name = tmp_name

    scene = os.path.join(root, name, f"{name}.db" )

    sqlite_util.resume_scene(scene, name)
    sqlite_util.mark_resumed_scene(history_db, name)
    sqlite_util.update_current_scene(history_db, name)
    
    display.display_resume_scene(name)