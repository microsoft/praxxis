"""
tests scene utilities
"""
from src.mtool.scene import scene

def init_scene(setup, init_root, history_db, default_scene_name, scene_db = ""):
    """
    tests initializing of scenes
    """
    import os

    scene.init_scene(scene_db, history_db, default_scene_name)
    assert os.path.exists(scene_db)