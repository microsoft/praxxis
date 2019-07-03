import pytest 

@pytest.mark.skip(reason="telemetry isn't up and running yet")
def test_empty_history(history_db, library_db, current_scene_db):
    from src.mtool.scene import history

    notebooks = history.history(history_db, library_db, current_scene_db)
    assert len(notebooks) == 0

@pytest.mark.skip(reason="telemetry isn't up and running yet")
def test_short_history(history_db, library_db, current_scene_db, generate_short_history):
    from src.mtool.scene import history

    notebooks = history.history(history_db, library_db, current_scene_db)
    assert len(notebooks) == 0
    