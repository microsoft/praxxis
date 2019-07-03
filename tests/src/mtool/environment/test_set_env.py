import argparse 

def test_set_env(setup, scene_root, history_db, current_scene_db, start, stop):
    from src.mtool.environment import set_env
    from src.mtool.environment import list_env
    from src.mtool.environment import delete_env
    from tests.src.mtool.util import dummy_object

    name1 = dummy_object.make_dummy_environment("test", "test")

    set_env.set_env(name1, scene_root, history_db, current_scene_db)
    result = list_env.list_env(current_scene_db, start, stop)

    assert result[0][0] == name1.name 
    assert result[0][1] == name1.value

    delete_env.delete_env(name1, scene_root, history_db, current_scene_db)    