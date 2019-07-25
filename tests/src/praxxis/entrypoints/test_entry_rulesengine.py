from src.praxxis.entrypoints import entry_rulesengine
from tests.src.praxxis.util import dummy_object

def test_new_ruleset(setup, rulesengine_root, rulesengine_db):
    name1 = dummy_object.make_dummy_ruleset("generated_one_ruleset")
    entry_rulesengine.new_ruleset(name1, rulesengine_root, rulesengine_db)

    from src.praxxis.sqlite import sqlite_rulesengine
    ruleset_list = sqlite_rulesengine.get_all_rulesets(rulesengine_db, start=1, end=10)

    assert ruleset_list[0][0] == name1.name