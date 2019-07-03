import pytest

@pytest.fixture(scope="function")
def set_many_envs(scene_root, history_db, current_scene_db):
    from src.mtool.environment import set_env
    from src.mtool.environment import delete_env
    from tests.src.mtool.util import dummy_name_object

    name1 = dummy_name_object.make_dummy_object("test", "test")
    set_env.set_env(name1, scene_root, history_db, current_scene_db)
    
    name2 = dummy_name_object.make_dummy_object("test1", "test")
    set_env.set_env(name2, scene_root, history_db, current_scene_db)

    yield
    delete_env.delete_env(name1, scene_root, history_db, current_scene_db)
    delete_env.delete_env(name2, scene_root, history_db, current_scene_db)

