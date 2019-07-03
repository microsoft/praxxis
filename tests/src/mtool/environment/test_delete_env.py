import argparse 

def test_delete_one_env(setup, scene_root, history_db, current_scene_db, start, stop):
    from src.mtool.environment import delete_env
    from src.mtool.environment import list_env
    from tests.src.mtool.util import dummy_name_object

    name1 = dummy_name_object.make_dummy_object("test")

    print(scene_root)
    print(history_db)
    print(current_scene_db)
    
    delete_env.delete_env(name1, scene_root, history_db, current_scene_db)

    result = list_env.list_env(name1, scene_root, history_db, current_scene_db, start, stop)

    assert result == []
    

def test_delete_many_env(setup, set_many_envs, scene_root, history_db, current_scene_db, start, stop):
    from src.mtool.environment import delete_env
    from src.mtool.environment import list_env
    from tests.src.mtool.util import dummy_name_object

    name1 = dummy_name_object.make_dummy_object("test1")

    result = list_env.list_env(name1, scene_root, history_db, current_scene_db, start, stop)
    assert len(result) == 2

    delete_env.delete_env(name1, scene_root, history_db, current_scene_db)
    result = list_env.list_env(name1, scene_root, history_db, current_scene_db, start, stop)

    assert len(result) == 1
    