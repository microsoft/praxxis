from tests.src import global_vars

def test_new_scene(init_root, default_scene_name, scene_root, history_db):
    from src.mtool.scene import new_scene
    import os 

    db_file = new_scene.new_scene(default_scene_name, scene_root, history_db)
    assert not os.path.exists(db_file)

    return db_file