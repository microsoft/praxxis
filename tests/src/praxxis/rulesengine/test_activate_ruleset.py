
import pytest

def test_activate_ruleset(setup, create_deactivated_ruleset, rulesengine_db):
    """
    tests activate_ruleset functionality. Requires that setup is run and there is a ruleset inactive.
    """
    from src.praxxis.rulesengine import activate_ruleset
    from tests.src.praxxis.util import dummy_object
    import os

    name1 = dummy_object.make_dummy_ruleset("generated_deactivated_ruleset")

    result = activate_ruleset.activate_ruleset(name1, rulesengine_db)
    
    assert result == name1.name

def test_activate_ruleset_nonexistent(setup, rulesengine_db):
    from src.praxxis.rulesengine import activate_ruleset
    from tests.src.praxxis.util import dummy_object
    from src.praxxis.util import error
    from src.praxxis.display import display_error
    name1 = dummy_object.make_dummy_ruleset("nonexistent_ruleset")

    try:
        activate_ruleset.activate_ruleset(name1, rulesengine_db)
    except error.RulesetNotFoundError as e:
        assert str(e) == display_error.ruleset_not_found_error(name1.name)
        
def test_activate_ruleset_already_active(setup, create_one_ruleset, rulesengine_db):
    from src.praxxis.rulesengine import activate_ruleset
    from tests.src.praxxis.util import dummy_object
    from src.praxxis.util import error
    from src.praxxis.display import display_error
    import os

    name1 = dummy_object.make_dummy_ruleset("generated_one_ruleset")

    try:
        activate_ruleset.activate_ruleset(name1, rulesengine_db)
    except error.RulesetActiveError as e:
        assert str(e) == display_error.ruleset_active_error(name1.name)
