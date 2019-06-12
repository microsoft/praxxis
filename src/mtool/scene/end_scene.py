"""
This file calls the function to end the current scence.

Dependencies within mtool: mtool/mtool.py
"""

import os

def end_scene(args, root):
    """Ends a scene"""
    from src.mtool.util import sqlite_util
    
    if hasattr(args, "name"):
        name = args.name
    else:
        name = args

    scene = os.path.join(root, name, f"{name}.db" )
    current_scene = os.path.join(root, "current_scene.db")

    if sqlite_util.mark_ended_scene(current_scene, name):
        sqlite_util.end_scene(scene, name)
        
    