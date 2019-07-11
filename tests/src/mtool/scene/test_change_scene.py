"""
Tests the change scene functionality
"""

def test_change_scene(setup, create_many_scenes, init_root, scene_root, history_db, default_scene_name):
    import argparse
    from src.mtool.scene import current_scene
    from src.mtool.scene import change_scene
    from src.mtool.scene import list_scene

    scene = current_scene.current_scene(scene_root, history_db)
    status = change_scene.change_scene(default_scene_name, scene_root, history_db)
    
    assert status == default_scene_name
    assert status != scene
