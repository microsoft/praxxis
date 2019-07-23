import pytest
import mock

@pytest.mark.skip(reason="broken and not working")
def test_add_rule(setup, create_one_ruleset, mock_input_str, rulesengine_db, library_db, history_db, start, stop):
    from src.praxxis.rulesengine import add_rule_to_ruleset
    from tests.src.praxxis.util import dummy_object

    name1 = dummy_object.make_dummy_ruleset("generated_one_ruleset")
    add_rule_to_ruleset.add_rule_to_ruleset(name1, rulesengine_db, library_db, history_db, start, stop)
        
    """
    with mock.patch.object(__builtins__, 'input', lambda: 'some_input'):
        assert 0
    """
    