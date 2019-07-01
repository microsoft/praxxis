from tests.src import global_vars

def test_new_scene(name = global_vars.DEFAULT_SCENE_NAME, scene_root = global_vars.SCENE_ROOT, history_db = global_vars.HISTORY_DB):
    from src.mtool.scene import new_scene
    import os 

    db_file = new_scene.new_scene(name, scene_root, history_db)
    assert db_file == os.path.join(scene_root, name)

    db_file = new_scene.new_scene(name, scene_root, history_db)
    assert db_file == os.path.join(scene_root, name, '-1')


def clear_new_scenes(scene_root = global_vars.SCENE_ROOT):
    

    
