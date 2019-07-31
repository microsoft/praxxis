"""
this tests the deactivate ruleset functionality of praxxis
"""

import pytest 

def test_deactivate_ruleset(setup, create_one_ruleset, rulesengine_db):
    """
    tests deactivate_ruleset functionality. Requires that setup is run and there is a ruleset active.
    """
    from src.praxxis.rulesengine import deactivate_ruleset
    from tests.src.praxxis.util import dummy_object
    import os

    name1 = dummy_object.make_dummy_ruleset("generated_one_ruleset")

    result = deactivate_ruleset.deactivate_ruleset(name1, rulesengine_db)
    
    assert result == name1.name

def test_deactivate_ruleset_nonexistent(setup, rulesengine_db):
    from src.praxxis.rulesengine import deactivate_ruleset
    from tests.src.praxxis.util import dummy_object
    from src.praxxis.util import error
    from src.praxxis.display import display_error
    name1 = dummy_object.make_dummy_ruleset("nonexistent_ruleset")

    try:
        deactivate_ruleset.deactivate_ruleset(name1, rulesengine_db)
    except error.RulesetNotFoundError as e:
        assert str(e) == display_error.ruleset_not_found_error(name1.name)

def test_deactivate_ruleset_already_inactive(setup, rulesengine_db, create_deactivated_ruleset):
    from src.praxxis.rulesengine import deactivate_ruleset
    from tests.src.praxxis.util import dummy_object
    from src.praxxis.display import display_error
    from src.praxxis.util import error

    name1 = dummy_object.make_dummy_ruleset("generated_deactivated_ruleset")

    try:
        deactivate_ruleset.deactivate_ruleset(name1, rulesengine_db)
    except error.RulesetNotActiveError as e:
        assert str(e) == display_error.ruleset_not_active_error(name1.name)
    