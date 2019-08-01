def test_pull_library_notebook(setup, add_test_library, library_db, current_scene_db, query_start, query_end):
    from src.praxxis.parameter import pull_param
    from tests.src.praxxis.util import dummy_object
    from src.praxxis.parameter import list_param

    # args = dummy_object.make_dummy_library()

    # params = list_param.list_param(current_scene_db, query_start, query_end)
    # assert len(params) == 0
    # pull_param.pull_library_parameter(args, library_db, current_scene_db)
    # assert len(params) == 2
