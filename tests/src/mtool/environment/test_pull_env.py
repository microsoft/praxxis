def test_pull_library_notebook(setup, add_test_library, library_db, current_scene_db, start, stop):
    from src.mtool.environment import pull_env
    from tests.src.mtool.util import dummy_object
    from src.mtool.environment import list_env

    # args = dummy_object.make_dummy_library()

    # envs = list_env.list_env(current_scene_db, start, stop)
    # assert len(envs) == 0
    # pull_env.pull_library_environment(args, library_db, current_scene_db)
    # assert len(envs) == 2
