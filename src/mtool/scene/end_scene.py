"""
This file calls the function to end the current scence.

Dependencies within mtool: mtool/mtool.py
"""

import os

def end_scene(args, root, history_db):
    """Ends a scene"""
    from src.mtool.util import sqlite_util
    from src.mtool.cli import display
    
    if hasattr(args, "name"):
        name = args.name
    else:
        name = args

    scene = os.path.join(root, name, f"{name}.db" )

    if sqlite_util.mark_ended_scene(history_db, name):
        sqlite_util.end_scene(scene, name)
        display.display_end_scene_success(name)
    else:
        display.last_active_scene_error(name)

        
    