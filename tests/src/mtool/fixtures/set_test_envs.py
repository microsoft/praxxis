import pytest

@pytest.fixture(scope="function")
def set_many_envs(scene_root, history_db, current_scene_db):
    import argparse
    from src.mtool.environment import set_env

    namespace = argparse.Namespace

    namespace.name = 'test'
    namespace.value = 'test'

    set_env.set_env(namespace, scene_root, history_db, current_scene_db)

    namespace.name = 'test1'
    namespace.value = 'test'

    set_env.set_env(namespace, scene_root, history_db, current_scene_db)
