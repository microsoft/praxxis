"""
This file lists all of the environment variables
"""

import os

def list_env(args, scene_root, history_db, start, end):
    """lists the environment variables by getting them out of the scene"""
    from src.mtool.util import sqlite_util
    from src.mtool.cli import display
    
    scene = sqlite_util.get_current_scene(history_db)

    directory = os.path.join(scene_root, scene)
    db_file = os.path.join(directory, f"{scene}.db")

    display.display_list_env(sqlite_util.list_env(db_file, start, end))
