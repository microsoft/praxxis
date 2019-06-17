"""
This file displays the history in the current scene.
"""

def history(args, history_db, current_scene_db):
    """displays the notebook history of the sceen"""
    from src.mtool.util import sqlite_util
    from src.mtool.cli import display

    curr_scene = sqlite_util.get_current_scene(history_db)
    
    notebook_history = sqlite_util.get_notebook_history(current_scene_db)
    display.display_history(curr_scene, notebook_history)
