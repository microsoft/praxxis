import pytest

@pytest.fixture(scope="function")
def set_many_envs(scene_root, history_db, current_scene_db):
    from src.mtool.environment import set_env
    from src.mtool.environment import delete_env
    from tests.src.mtool.util import dummy_object
    from src.mtool.util import error

    name1 = dummy_object.make_dummy_environment("generated_multiple_env", "test")
    set_env.set_env(name1, scene_root, history_db, current_scene_db)
    
    name2 = dummy_object.make_dummy_environment("generated_multiple_env1", "test")
    set_env.set_env(name2, scene_root, history_db, current_scene_db)
    yield
    try:
        delete_env.delete_env(name1, scene_root, history_db, current_scene_db)
        delete_env.delete_env(name2, scene_root, history_db, current_scene_db)
    except error.EnvNotFoundError:
        pass


@pytest.fixture(scope="function")
def set_one_env(scene_root, history_db, current_scene_db):
    from src.mtool.environment import set_env
    from src.mtool.environment import delete_env
    from tests.src.mtool.util import dummy_object
    from src.mtool.util import error


    name1 = dummy_object.make_dummy_environment("generated_single_env", "test")
    set_env.set_env(name1, scene_root, history_db, current_scene_db)
    
    yield 
    try:
        delete_env.delete_env(name1, scene_root, history_db, current_scene_db)
    except error.EnvNotFoundError:
        pass

