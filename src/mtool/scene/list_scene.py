"""
This file calls a function to list all scenes.

Dependencies within mtool: mtool/mtool.py
"""

import os

def list_scene(root):
    from src.mtool.util import sqlite_util
    current_scene = os.path.join(root, "current_scene.db")
    ended_scenes = ", ".join(list(sum(sqlite_util.get_ended_scenes(current_scene), ())))
    active_scenes = ", ".join(list(sum(sqlite_util.get_active_scenes(current_scene), ())))
    current_scene = sqlite_util.get_current_scene(current_scene)
    ##TODO: print this properly
    print(f'ended Scenes : {ended_scenes}')
    print(f'active Scenes : {active_scenes}')
    print(f'current Scene : {current_scene}')

