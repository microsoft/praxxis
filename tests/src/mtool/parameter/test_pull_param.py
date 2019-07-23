def test_pull_library_notebook(setup, add_test_library, library_db, current_scene_db, start, stop):
    from src.mtool.parameter import pull_param
    from tests.src.mtool.util import dummy_object
    from src.mtool.parameter import list_param

    # args = dummy_object.make_dummy_library()

    # params = list_param.list_param(current_scene_db, start, stop)
    # assert len(params) == 0
    # pull_param.pull_library_parameter(args, library_db, current_scene_db)
    # assert len(params) == 2
