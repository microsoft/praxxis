import argparse 

def test_set_param(setup, scene_root, history_db, current_scene_db, start, stop):
    from src.mtool.parameter import set_param
    from src.mtool.parameter import list_param
    from src.mtool.parameter import delete_param
    from tests.src.mtool.util import dummy_object

    name1 = dummy_object.make_dummy_parameter("test", "test")

    set_param.set_param(name1, scene_root, history_db, current_scene_db)
    result = list_param.list_param(current_scene_db, start, stop)

    assert result[0][0] == name1.name 
    assert result[0][1] == name1.value

    delete_param.delete_parameter(name1, scene_root, history_db, current_scene_db)    