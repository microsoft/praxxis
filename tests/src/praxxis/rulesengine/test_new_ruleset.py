import pytest

def test_new_ruleset(setup, rulesengine_root, rulesengine_db, query_start, stop):
    from src.praxxis.rulesengine import new_ruleset
    from tests.src.praxxis.util import dummy_object
    from src.praxxis.sqlite import sqlite_rulesengine


    name1 = dummy_object.make_dummy_ruleset("new_ruleset")
    message = new_ruleset.new_ruleset(name1, rulesengine_root, rulesengine_db)

    assert message == name1.name

    rulesets = sqlite_rulesengine.get_all_rulesets(rulesengine_db, query_start, stop)
    assert len(rulesets) == 1
    assert rulesets[0][0] == name1.name

    
    sqlite_rulesengine.clear_ruleset_list(rulesengine_db)