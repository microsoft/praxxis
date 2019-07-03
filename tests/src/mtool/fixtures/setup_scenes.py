import pytest

@pytest.fixture(scope="function")
def create_many_scenes(scene_root, init_root, history_db, current_scene_db, default_scene_name):
    import argparse
    import shutil
    import os
    from src.mtool.scene import new_scene
    from src.mtool.scene import delete_scene
    from src.mtool.scene import list_scene

    name1 = argparse.Namespace
    name1.name = default_scene_name

    name2 = argparse.Namespace
    name2.name = default_scene_name
    
    new_scene.new_scene(name1, scene_root, history_db)
    new_scene.new_scene(name2, scene_root, history_db)

    yield 
    shutil.rmtree(scene_root)
    os.mkdir(scene_root)
    new_scene.new_scene(default_scene_name, scene_root, history_db)
    