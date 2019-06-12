"""
This file calls a function to change the current scene.

Dependencies within mtool: mtool/mtool.py
"""

import os

def change_scene(args, root):
    """Calls mtool method to change the current scene"""
    from src.mtool.util import sqlite_util

    if hasattr(args, "name"):
        name = args.name
    else:
        name = args

    current_scene = os.path.join(root, "current_scene.db")
    sqlite_util.update_current_scene(current_scene, name)

