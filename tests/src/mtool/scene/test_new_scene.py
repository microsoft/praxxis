"""
this file tests the creation of a new scene 
"""

def test_new_scene(setup, init_root, default_scene_name, scene_root, history_db):
    """
    tests creating a new scene. depends on setup. 
    """
    from src.mtool.scene import new_scene
    import os 

    db_file = new_scene.new_scene(default_scene_name, scene_root, history_db)
    assert not os.path.exists(db_file)

    return db_file
    