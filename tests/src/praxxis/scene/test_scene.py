"""
tests scene utilities
"""
from src.praxxis.scene import scene

def init_scene(setup, init_root, history_db, default_scene_name, scene_db = ""):
    """
    tests initializing of scenes
    """
    import os
    from src.praxxis.scene import delete_scene

    scene_data = scene.init_scene(scene_db, history_db, default_scene_name)[0]
    assert os.path.exists(scene_data)
    delete_scene.delete_scene(scene_data[1], scene_data[0], history_db)
