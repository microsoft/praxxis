import pytest

@pytest.fixture(scope="function")
def create_one_ruleset(rulesengine_root, rulesengine_db):
    from src.praxxis.rulesengine import new_ruleset
    from src.praxxis.rulesengine import remove_ruleset
    from tests.src.praxxis.util import dummy_object
    from src.praxxis.util import error

    name1 = dummy_object.make_dummy_ruleset("generated_one_ruleset")
    new_ruleset.new_ruleset(name1, rulesengine_root, rulesengine_db)
    yield
    try:
        remove_ruleset.remove_ruleset(name1, rulesengine_db)
    except error.RulesetNotFoundError:
        pass

@pytest.fixture(scope="function")
def create_one_ruleset_one_rule(rulesengine_root, rulesengine_db):
    from src.praxxis.rulesengine import new_ruleset
    from src.praxxis.rulesengine import remove_ruleset
    from src.praxxis.sqlite import sqlite_rulesengine
    from tests.src.praxxis.util import dummy_object
    from src.praxxis.util import error

    name1 = dummy_object.make_dummy_ruleset("generated_ruleset_with_rule")
    new_ruleset.new_ruleset(name1, rulesengine_root, rulesengine_db)
    # ADD RULE TO SQLITE
    ruleset_path = sqlite_rulesengine.get_ruleset_path(rulesengine_db, name1.name)
    sqlite_rulesengine.add_rule(ruleset_path, "testing", ["f1, f3"], ["out1","out2"],[('testing', 1, 'pred1', 'lib', None),('testing', 2, 'pred2', 'lib', None)])
    yield
    try:
        remove_ruleset.remove_ruleset(name1, rulesengine_db)
    except error.RulesetNotFoundError:
        pass

@pytest.fixture(scope="function")
def create_deactivated_ruleset(rulesengine_root, rulesengine_db):
    from src.praxxis.rulesengine import new_ruleset
    from src.praxxis.rulesengine import deactivate_ruleset
    from src.praxxis.rulesengine import remove_ruleset
    from tests.src.praxxis.util import dummy_object
    from src.praxxis.util import error

    name1 = dummy_object.make_dummy_ruleset("generated_deactivated_ruleset")
    new_ruleset.new_ruleset(name1, rulesengine_root, rulesengine_db)
    deactivate_ruleset.deactivate_ruleset(name1, rulesengine_db)
    yield
    try:
        remove_ruleset.remove_ruleset(name1, rulesengine_db)
    except error.RulesetNotFoundError:
        pass