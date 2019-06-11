"""
This file sets up the toml overrides for the current scene.

Dependencies within mtool: mtool/mtool.py
"""

import os
import sys

def current_scene(args):
    """Sets up environment for current scene""" 
    from src.mtool.scene import scene
    from src.mtool.util import sqlite_util

    root = os.path.join(os.getenv('APPDATA'),"mtool","scene")
    default_scene_name = 'scene'

    current_scene = os.path.join(root, "current_scene.db")

    if not os.path.exists(root):
        os.mkdir(root)
        
    if not os.path.exists(current_scene):
        scene.new_scene(default_scene_name, default_scene_name)
        sqlite_util.init_current_scene(os.path.join(root, "current_scene.db"), default_scene_name)
        print("Created current_scene")

    print(sqlite_util.get_current_scene(current_scene)) 
    return("nya?")   
    