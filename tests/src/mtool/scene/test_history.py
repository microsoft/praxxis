import pytest 

def test_empty_history(setup, history_db, library_db, current_scene_db):
    from src.mtool.scene import history

    notebooks = history.history(history_db, library_db, current_scene_db)
    assert len(notebooks) == 0

def test_short_history(setup, history_db, library_db, current_scene_db, generate_short_history):
    from src.mtool.scene import history

    notebooks = history.history(history_db, library_db, current_scene_db)
    assert len(notebooks) == 1
    