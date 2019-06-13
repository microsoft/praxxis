"""
This file sets up the toml overrides for the current scene.

Dependencies within mtool: mtool/mtool.py
"""

import os

def current_scene(root, history_db):
    """Sets up environment for current scene""" 
    from src.mtool.scene import new_scene
    from src.mtool.util import sqlite_util

    default_scene_name = 'scene'
    if not os.path.exists(root):
        os.mkdir(root)
        
    if not os.path.exists(history_db):
        sqlite_util.init_current_scene(history_db, default_scene_name)
        new_scene.new_scene(default_scene_name, root, history_db)
        print("Created history db")
##TODO: REMOVE PRINTS, ENVIRONMENT LOADING ??
    print(f'Current Scene: {sqlite_util.get_current_scene(history_db)}') 
    return history_db
    
    