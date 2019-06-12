"""
This file calls the function to resume a previously used scene.

Dependencies within mtool: mtool/mtool.py
"""

import os

def resume_scene(args, root):
    """Resumes a scene"""
    from src.mtool.util import sqlite_util

    if hasattr(args, "name"):
        name = args.name
    else:
        name = args

    scene = os.path.join(root, name, f"{name}.db" )
    current_scene = os.path.join(root, "current_scene.db")

    sqlite_util.resume_scene(scene, name)
    sqlite_util.update_current_scene(current_scene, name)
