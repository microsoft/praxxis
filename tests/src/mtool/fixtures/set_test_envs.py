import pytest

@pytest.fixture(scope="function")
def set_many_envs(scene_root, history_db, current_scene_db):
    import argparse
    from src.mtool.environment import set_env
    from src.mtool.environment import delete_env

    env1 = argparse.Namespace

    env1.name = 'test'
    env1.value = 'test'

    set_env.set_env(env1, scene_root, history_db, current_scene_db)
    
    env2 = argparse.Namespace

    env2.name = 'test1'
    env2.value = 'test'

    set_env.set_env(env2, scene_root, history_db, current_scene_db)

    yield 
    delete_env.delete_env(env1, scene_root, history_db, current_scene_db)
    delete_env.delete_env(env2, scene_root, history_db, current_scene_db)