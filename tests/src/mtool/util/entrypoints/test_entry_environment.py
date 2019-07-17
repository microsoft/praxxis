from src.mtool.util.entrypoints import entry_environment
from tests.src.mtool.util import dummy_object

def test_view_library_env(setup, add_test_library, scene_root, history_db, library_db, current_scene_db, start, stop):
    from src.mtool.environment import list_env

    library_envs = list_env.list_library_env("test_notebooks", library_db, current_scene_db)
    envs = dummy_object.make_dummy_notebook_envs()

    entry_environment.view_library_env("test_notebooks", scene_root, history_db, library_db, current_scene_db)
    assert envs.environment == library_envs


def test_list_env(setup, set_one_env, scene_root, history_db, start, stop, current_scene_db):
    from src.mtool.environment import list_env
    entry_environment.list_env("", scene_root, history_db, start, stop, current_scene_db)
    
    assert len(list_env.list_env(current_scene_db, start, stop)) == 1


def test_delete_env(setup, set_one_env, scene_root, history_db, current_scene_db, start, stop):
    from src.mtool.environment import list_env

    entry_environment.delete_env("generated_single_env", scene_root, history_db, current_scene_db)
    assert len(list_env.list_env(current_scene_db, start, stop)) == 0
    


def test_set_env(setup, scene_root, history_db, current_scene_db):
    from src.mtool.environment import delete_env
    from src.mtool.util import error

    env = dummy_object.make_dummy_environment("test_set_env", "test")

    entry_environment.set_env(env, scene_root, history_db)
    try:
        delete_env.delete_env(env, scene_root, history_db, current_scene_db)
    except error.EnvNotFoundError:
        assert 0
    else:
        assert 1


def test_view_notebook_env(setup, add_test_library, scene_root, library_db, history_db, current_scene_db, start, stop):
    import os
    from src.mtool.environment import list_env

    notebook = dummy_object.make_dummy_notebook_params()
    dummy_envs = dummy_object.make_dummy_notebook_envs()
    entry_environment.view_notebook_env(notebook, scene_root, library_db, history_db, current_scene_db)

    envs = list_env.list_notebook_env(notebook, library_db, current_scene_db)

    assert dummy_envs.environment ==  envs
