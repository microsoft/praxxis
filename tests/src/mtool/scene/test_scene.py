from src.mtool.scene import scene
from tests.src import global_vars

def test_init_scene(init_root, history_db, default_scene_name, scene_db = ""):
    import os
    print(scene_db)

    scene.init_scene(scene_db, history_db, default_scene_name)
    assert os.path.exists(scene_db)