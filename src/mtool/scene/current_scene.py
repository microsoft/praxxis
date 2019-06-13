"""
This file sets up the toml overrides for the current scene.

Dependencies within mtool: mtool/mtool.py
"""

import os

def current_scene(root, history_db):
    """Sets up environment for current scene""" 
    from src.mtool.util import sqlite_util
    from src.mtool.scene import scene
    from src.mtool.cli import display

    scene.init_scene(root, history_db)
    display.display_current_scene(sqlite_util.get_current_scene(history_db))
    
    