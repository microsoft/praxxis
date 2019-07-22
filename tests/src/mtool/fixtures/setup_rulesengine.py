import pytest

@pytest.fixture(scope="function")
def create_one_ruleset(rulesengine_root, rulesengine_db):
    from src.mtool.rulesengine import new_ruleset
    from src.mtool.rulesengine import remove_ruleset
    from tests.src.mtool.util import dummy_object
    from src.mtool.util import error

    name1 = dummy_object.make_dummy_ruleset("generated_one_ruleset")
    new_ruleset.new_ruleset(name1, rulesengine_root, rulesengine_db)
    yield
    try:
        remove_ruleset.remove_ruleset(name1, rulesengine_db)
    except error.RulesetNotFoundError:
        pass

@pytest.fixture(scope="function")
def create_deactivated_ruleset(rulesengine_root, rulesengine_db):
    from src.mtool.rulesengine import new_ruleset
    from src.mtool.rulesengine import deactivate_ruleset
    from src.mtool.rulesengine import remove_ruleset
    from tests.src.mtool.util import dummy_object
    from src.mtool.util import error

    name1 = dummy_object.make_dummy_ruleset("generated_deactivated_ruleset")
    new_ruleset.new_ruleset(name1, rulesengine_root, rulesengine_db)
    deactivate_ruleset.deactivate_ruleset(name1, rulesengine_db)
    yield
    try:
        remove_ruleset.remove_ruleset(name1, rulesengine_db)
    except error.RulesetNotFoundError:
        pass
