from src.mtool.environment import delete_env

def test_delete_env(args, scene_root, history_db, current_scene_db):
    delete_env.delete_env(args, scene_root, history_db, current_scene_db)