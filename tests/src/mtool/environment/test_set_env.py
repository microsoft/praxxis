import argparse 

def test_set_env(setup, setup_sqlite, scene_root, history_db, current_scene_db, start, stop):
    from src.mtool.environment import set_env
    from src.mtool.environment import list_env

    namespace = argparse.Namespace
    namespace.name = 'test'
    namespace.value = 'test'

    set_env.set_env(namespace, scene_root, history_db, current_scene_db)
    result = list_env.list_env(namespace, scene_root, history_db, current_scene_db, start, stop)

    assert result[0][0] == namespace.name 
    assert result[0][1] == namespace.value
    