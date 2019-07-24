import pytest

def test_import_ruleset_toml(setup, rulesengine_root, rulesengine_db):
    from src.praxxis.rulesengine import import_ruleset
    from tests.src.praxxis.util import dummy_object
    from src.praxxis.rulesengine import remove_ruleset
    import os

    path_to_toml = os.path.join(os.path.dirname(__file__), "..",  "..", "..", "test_importables", "test_toml_ruleset.toml")
    
    name1 = dummy_object.make_dummy_path(path_to_toml)
    message = import_ruleset.import_ruleset(name1, rulesengine_root, rulesengine_db)

    assert message == "test_toml_ruleset"
    
    remove_ruleset.remove_ruleset(message, rulesengine_db)    

def test_import_ruleset__toml_duplicate_name(setup, rulesengine_root, rulesengine_db):
    from src.praxxis.rulesengine import import_ruleset
    from src.praxxis.sqlite import sqlite_rulesengine
    from tests.src.praxxis.util import dummy_object
    import os

    path_to_toml = os.path.join(os.path.dirname(__file__), "..",  "..", "..", "test_importables", "test_toml_ruleset.toml")

    assert sqlite_rulesengine.get_all_rulesets(rulesengine_db, 1, 100) == []

    name1 = dummy_object.make_dummy_path(path_to_toml)
    message1 = import_ruleset.import_ruleset(name1, rulesengine_root, rulesengine_db)
    message2 = import_ruleset.import_ruleset(name1, rulesengine_root, rulesengine_db)
    message3 = import_ruleset.import_ruleset(name1, rulesengine_root, rulesengine_db)

    assert message1 == "test_toml_ruleset"
    assert message2 == "test_toml_ruleset-1"
    assert message3 == "test_toml_ruleset-2"

    from src.praxxis.rulesengine import remove_ruleset
    
    remove_ruleset.remove_ruleset(message1, rulesengine_db)  
    remove_ruleset.remove_ruleset(message2, rulesengine_db)  
    remove_ruleset.remove_ruleset(message3, rulesengine_db)  
