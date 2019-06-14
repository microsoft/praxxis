"""
This file prints the history in the current scene.

Dependencies within mtool: mtool/mtool.py
"""
import os

from src.mtool.util import sqlite_util
from src.mtool.cli import display

counter = 0
items = []
uniquify = False
m = None

def history(args, history_db):
    """Calls display for every notebook in scene history"""

    # TODO: fix this mess
    curr_scene = sqlite_util.get_current_scene(history_db)
    curr_scene_path = os.path.join(os.path.dirname(history_db), curr_scene, curr_scene + ".db")
    
    notebook_history = sqlite_util.get_notebook_history(curr_scene_path)
    display.display_history(curr_scene, notebook_history)
    # TODO: update notebook list 

