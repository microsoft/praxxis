"""
this file tests the creation of a new scene 
"""

def test_new_scene(setup, init_root, default_scene_name, scene_root, history_db):
    """
    tests creating a new scene. depends on setup. 
    """
    from src.mtool.scene import new_scene
    from src.mtool.scene import delete_scene
    import os 

    scene_data = new_scene.new_scene(default_scene_name, scene_root, history_db)
    assert os.path.exists(scene_data[0])
    delete_scene.delete_scene(scene_data[1], scene_root, history_db)

