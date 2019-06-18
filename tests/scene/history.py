from src.mtool.scene import history

def test_history(args, history_db, current_scene_db):
    history.history(args, history_db, current_scene_db)