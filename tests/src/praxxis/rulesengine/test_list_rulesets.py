import pytest

def test_list_rulesets(setup, create_one_ruleset, create_one_ruleset_one_rule, create_deactivated_ruleset, rulesengine_db, query_start, query_end):
    from src.praxxis.rulesengine import list_rulesets
    from tests.src.praxxis.util import dummy_object
    from src.praxxis.sqlite import sqlite_rulesengine


    name1 = dummy_object.make_dummy_ruleset("generated_one_ruleset")
    name2 = dummy_object.make_dummy_ruleset("generated_ruleset_with_rule")
    name3 = dummy_object.make_dummy_ruleset("generated_deactivated_ruleset")
    
    result = list_rulesets.list_rulesets(name1, rulesengine_db, query_start, query_end)

    assert len(result) == 3
    for info in result:
        assert len(info) == 2
    assert result[0][0] == name1.name
    assert result[0][1] == 1 # active
    assert result[1][0] == name2.name
    assert result[1][1] == 1 # active
    assert result[2][0] == name3.name
    assert result[2][1] == 0 # inactive    
    