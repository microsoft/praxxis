from src.mtool.environment import set_env

def test_set_env(args, scene_root, history_db, current_scene_db):
    set_env.set_env(args, scene_root, history_db, current_scene_db)