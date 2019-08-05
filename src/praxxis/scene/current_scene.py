"""
This file displays the current scene from the scene history db
"""

def current_scene(scene_root, history_db):
    """calls the scene init and displays the current scene from the sqlite history db""" 
    from src.praxxis.sqlite import sqlite_scene
    from src.praxxis.scene import scene
    from src.praxxis.display import display_scene

    current_scene = sqlite_scene.get_current_scene(history_db)
    display_scene.display_current_scene(current_scene)
    return current_scene
