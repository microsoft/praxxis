from src.praxxis.entrypoints import entry_rulesengine
from tests.src.praxxis.util import dummy_object

def test_init_rulesengine(setup, rulesengine_root, rulesengine_db):
    from tests.src.praxxis.util import rmtree
    import os 

    assert os.path.exists(rulesengine_root)
    assert os.path.exists(rulesengine_db)
    os.remove(rulesengine_db)
    rmtree.rmtree(rulesengine_root)
    assert not os.path.exists(rulesengine_root)
    assert not os.path.exists(rulesengine_db)

    entry_rulesengine.init_rulesengine(rulesengine_root, rulesengine_db)

    assert os.path.exists(rulesengine_root)
    assert os.path.exists(rulesengine_db)


def test_new_ruleset(setup, rulesengine_root, rulesengine_db):
    name1 = dummy_object.make_dummy_ruleset("one_ruleset")
    entry_rulesengine.new_ruleset(name1, rulesengine_root, rulesengine_db)

    from src.praxxis.sqlite import sqlite_rulesengine
    ruleset_list = sqlite_rulesengine.get_all_rulesets(rulesengine_db, start=1, end=10)

    assert ruleset_list[0][0] == name1.name
    
    sqlite_rulesengine.clear_ruleset_list(rulesengine_db)


def test_remove_ruleset(setup, rulesengine_root, rulesengine_db, create_one_ruleset):
    name1 = dummy_object.make_dummy_ruleset("generated_one_ruleset")

    from src.praxxis.sqlite import sqlite_rulesengine
    ruleset_list = sqlite_rulesengine.get_all_rulesets(rulesengine_db, start=1, end=10)

    assert ruleset_list[0][0] == name1.name
    entry_rulesengine.remove_ruleset(name1, rulesengine_db)
    
    ruleset_list = sqlite_rulesengine.get_all_rulesets(rulesengine_db, start=1, end=10)

    assert len(ruleset_list) == 0
    