import pytest

def test_remove_ruleset(setup, create_one_ruleset, rulesengine_db):
    from src.mtool.rulesengine import remove_ruleset
    from tests.src.mtool.util import dummy_object

    name1 = dummy_object.make_dummy_ruleset("generated_one_ruleset")
    message = remove_ruleset.remove_ruleset(name1, rulesengine_db)

    assert message == name1.name

def test_remove_ruleset_nonexistent(setup, rulesengine_db):
    from src.mtool.rulesengine import remove_ruleset
    from tests.src.mtool.util import dummy_object
    from src.mtool.util import error

    name1 = dummy_object.make_dummy_ruleset("nonexistent_ruleset")

    try:
        remove_ruleset.remove_ruleset(name1, rulesengine_db)
    except error.RulesetNotFoundError:
        assert 1
