"""
This file calls a function to list all scenes.

Dependencies within mtool: mtool/mtool.py
"""

import os

def list_scene(root, history_db):
    from src.mtool.util import sqlite_util
    from src.mtool.cli import display
    
    ended_scenes = sqlite_util.get_ended_scenes(history_db)
    active_scenes = sqlite_util.get_active_scenes(history_db)
    current_scene = sqlite_util.get_current_scene(history_db)

    display.display_list_scene(ended_scenes, active_scenes, current_scene)

