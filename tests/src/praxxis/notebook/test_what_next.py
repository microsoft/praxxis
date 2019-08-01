import pytest

def test_what_next_rulesengine(setup, telemetry_db, current_scene_db, 
        library_db, rulesengine_db, query_start, stop, generate_short_history,
        create_one_ruleset_one_rule):
    from src.praxxis.notebook import what_next

    predictions = what_next.what_next("", telemetry_db, current_scene_db, library_db, rulesengine_db, query_start, stop)

    assert len(predictions) == 2
    assert predictions[0][0] == "pred1"
    assert predictions[1][0] == "pred2"
    