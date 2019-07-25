import pytest

def test_what_next_rulesengine(setup, telemetry_db, current_scene_db, 
        library_db, rulesengine_db, start, stop, generate_short_history,
        create_one_ruleset_one_rule):
    from src.praxxis.notebook import what_next

    
    assert 1