import pytest

def test_delete_rule(setup, monkeypatch, mock_input_str, create_one_ruleset_one_rule, rulesengine_db, library_db, create_one_scene,current_scene_db, start, stop):
    from src.praxxis.rulesengine import delete_rule_from_ruleset
    from src.praxxis.sqlite import sqlite_rulesengine
    from tests.src.praxxis.rulesengine import test_add_rule
    from tests.src.praxxis.util import dummy_object

    name1 = dummy_object.make_dummy_ruleset("generated_ruleset_with_rule")
    ruleset_path = sqlite_rulesengine.get_ruleset_path(rulesengine_db, name1.name)

    mock_in = input("")
    rulename = delete_rule_from_ruleset.delete_rule_from_ruleset(name1, rulesengine_db)
    assert rulename == mock_in

    # test database cleaning
    rules = sqlite_rulesengine.list_rules_in_ruleset(ruleset_path)
    filenames = sqlite_rulesengine.get_filenames(ruleset_path, rulename)
    outputs = sqlite_rulesengine.get_outputs(ruleset_path, rulename)
    predictions = sqlite_rulesengine.get_predictions(ruleset_path, [rulename])
    
    assert rules == [] 
    assert filenames == []
    assert outputs == []
    assert predictions == [] 
    

        