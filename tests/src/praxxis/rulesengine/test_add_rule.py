import pytest

def test_add_rule(setup, monkeypatch, create_one_ruleset, rulesengine_db, library_db, create_one_scene,current_scene_db, start, stop):
    from src.praxxis.rulesengine import add_rule_to_ruleset
    from tests.src.praxxis.util import dummy_object

    name1 = dummy_object.make_dummy_ruleset("generated_one_ruleset")
    mock_in = "testing"
    
    with monkeypatch.context() as m:
        m.setattr("builtins.input", lambda _: mock_in)
        rulename = add_rule_to_ruleset.add_rule_to_ruleset(name1, rulesengine_db, library_db, current_scene_db, start, stop)

    from src.praxxis.sqlite import sqlite_rulesengine
    
    # returns rulename, which is the same as the mocked input 
    assert rulename == mock_in

    # test database input
    ruleset_path = sqlite_rulesengine.get_ruleset_path(rulesengine_db, name1.name)
    rules = sqlite_rulesengine.list_rules_in_ruleset(ruleset_path)
    filenames = sqlite_rulesengine.get_filenames(ruleset_path, rulename)
    outputs = sqlite_rulesengine.get_outputs(ruleset_path, rulename)
    predictions = sqlite_rulesengine.get_predictions(ruleset_path, [rulename])
    
    assert rules == [(mock_in,)] # list of rules should only be that one 
    assert filenames == [(mock_in,)]
    assert outputs == [(mock_in,)]
    assert predictions == [(mock_in,None,None)] # has no library, no path
    