import pytest

@pytest.fixture(scope="function")
def create_many_scenes(scene_root, history_db, current_scene_db, default_scene_name):
    import argparse
    from src.mtool.scene import new_scene

    namespace = argparse.Namespace

    namespace.name = default_scene_name
    
    new_scene.new_scene(namespace, scene_root, history_db)
    new_scene.new_scene(namespace, scene_root, history_db)
