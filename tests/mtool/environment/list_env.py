from src.mtool.environment import list_env

def test_list_env(args, scene_root, history_db, start, end):
    list_env.list_env(args, scene_root, history_db, start, end)