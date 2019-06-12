"""
This file calls a function to list all scenes.

Dependencies within mtool: mtool/mtool.py
"""

import os

def list_scene(root, history_db):
    from src.mtool.util import sqlite_util
    ended_scenes = ", ".join(list(sum(sqlite_util.get_ended_scenes(history_db), ())))
    active_scenes = ", ".join(list(sum(sqlite_util.get_active_scenes(history_db), ())))
    current_scene = sqlite_util.get_current_scene(history_db)
    ##TODO: print this properly
    print(f'ended Scenes : {ended_scenes}')
    print(f'active Scenes : {active_scenes}')
    print(f'current Scene : {current_scene}')

