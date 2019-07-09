from src.mtool.util.entrypoints import entry_environment
from tests.src.mtool.util import dummy_object

def test_view_library_env(setup, add_test_library, scene_root, history_db, library_db, current_scene_db):
    envs = entry_environment.view_library_env("test_notebooks", scene_root, history_db, library_db, current_scene_db)
    assert len(envs) == 2


def test_list_env(setup, set_one_env, scene_root, history_db, start, stop, current_scene_db):
    envs = entry_environment.list_env("", scene_root, history_db, start, stop, current_scene_db)
    
    assert len(envs) == 1


def test_delete_env(setup, set_one_env, scene_root, history_db, current_scene_db):
    assert entry_environment.delete_env("generated_single_env", scene_root, history_db, current_scene_db) == "generated_single_env"


def test_set_env(setup, scene_root, history_db, current_scene_db):
    from src.mtool.environment import delete_env
    env = dummy_object.make_dummy_environment("test_set_env", "test")

    set_env = entry_environment.set_env(env, scene_root, history_db)
    assert set_env.name == "test_set_env"
    delete_env.delete_env(env, scene_root, history_db, current_scene_db)


def test_view_notebook_env(setup, add_test_library, library_db):
    import os

    notebook = dummy_object.make_dummy_notebook_params()
    envs = entry_environment.view_notebook_env(notebook, library_db)
    
    assert len(envs) == 2
