import pytest

def test_view_rules(setup, create_one_ruleset_one_rule, rulesengine_db):
    from src.praxxis.rulesengine import view_rules
    from tests.src.praxxis.util import dummy_object

    name1 = dummy_object.make_dummy_ruleset("generated_ruleset_with_rule")
    ##
    # The rule in create_one_ruleset_one_rule:
    # "testing": ["f1, f3"]["out1","out2"] = [('testing', 1, 'pred1', 'lib', None),('testing', 2, 'pred2', 'lib', None)])
    ## 
    message = view_rules.view_rules(name1, rulesengine_db)

    assert len(message) == 1
    assert message[0][0] == "testing"
    