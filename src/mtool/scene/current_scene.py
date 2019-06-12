"""
This file sets up the toml overrides for the current scene.

Dependencies within mtool: mtool/mtool.py
"""

import os

def current_scene(root):
    """Sets up environment for current scene""" 
    from src.mtool.scene import new_scene
    from src.mtool.util import sqlite_util

    default_scene_name = 'scene'

    current_scene = os.path.join(root, "current_scene.db")

    if not os.path.exists(root):
        os.mkdir(root)
        
    if not os.path.exists(current_scene):
        sqlite_util.init_current_scene(os.path.join(root, "current_scene.db"), default_scene_name)
        print("Created current_scene")
        new_scene.new_scene(default_scene_name, root)


##TODO: REMOVE PRINTS, ENVIRONMENT LOADING ??

    print(f'Current Scene: {sqlite_util.get_current_scene(current_scene)}') 
    return current_scene
    
    