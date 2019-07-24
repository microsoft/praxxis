import pytest

def test_add_rule(setup, create_one_ruleset, mock_input_str, rulesengine_db, library_db, create_one_scene,current_scene_db, start, stop):
    from src.praxxis.rulesengine import add_rule_to_ruleset
    from tests.src.praxxis.util import dummy_object

    name1 = dummy_object.make_dummy_ruleset("generated_one_ruleset")
    add_rule_to_ruleset.add_rule_to_ruleset(name1, rulesengine_db, library_db, current_scene_db, start, stop)
        