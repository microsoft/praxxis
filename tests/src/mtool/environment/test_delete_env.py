import argparse 

def test_delete_one_env(setup, setup_sqlite, scene_root, history_db, current_scene_db, start, stop):
    from src.mtool.environment import delete_env
    from src.mtool.environment import list_env

    namespace = argparse.Namespace
    namespace.name = 'test'

    print(scene_root)
    print(history_db)
    print(current_scene_db)
    
    delete_env.delete_env(namespace, scene_root, history_db, current_scene_db)

    result = list_env.list_env(namespace, scene_root, history_db, current_scene_db, start, stop)

    assert result == []
    

def test_delete_many_env(setup, setup_sqlite, set_many_envs, scene_root, history_db, current_scene_db, start, stop):
    from src.mtool.environment import delete_env
    from src.mtool.environment import list_env

    namespace = argparse.Namespace
    namespace.name = 'test1'

    result = list_env.list_env(namespace, scene_root, history_db, current_scene_db, start, stop)
    assert len(result) == 2

    delete_env.delete_env(namespace, scene_root, history_db, current_scene_db)
    result = list_env.list_env(namespace, scene_root, history_db, current_scene_db, start, stop)

    assert len(result) == 1
    