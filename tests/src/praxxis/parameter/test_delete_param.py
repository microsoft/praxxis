import argparse 

def test_delete_one_param(setup, set_one_param, scene_root, history_db, current_scene_db, query_start, query_end):
    from src.praxxis.parameter import delete_param
    from src.praxxis.parameter import list_param
    from tests.src.praxxis.util import dummy_object

    name1 = dummy_object.make_dummy_object("generated_single_param")

    result = list_param.list_param(current_scene_db, query_start, query_end)
    assert len(result) == 1
    
    delete_param.delete_parameter(name1, scene_root, history_db, current_scene_db)
    result = list_param.list_param(current_scene_db, query_start, query_end)

    assert result == []
    

def test_delete_many_param(setup, set_many_params, scene_root, history_db, current_scene_db, query_start, query_end):
    from src.praxxis.parameter import delete_param
    from src.praxxis.parameter import list_param
    from tests.src.praxxis.util import dummy_object
    
    name1 = dummy_object.make_dummy_object("generated_multiple_param")
    name2 = dummy_object.make_dummy_object("generated_multiple_param1")

    result = list_param.list_param(current_scene_db, query_start, query_end)
    assert len(result) == 2

    delete_param.delete_parameter(name1, scene_root, history_db, current_scene_db)
    delete_param.delete_parameter(name2, scene_root, history_db, current_scene_db)
    result = list_param.list_param(current_scene_db, query_start, query_end)
    assert len(result) == 0
    