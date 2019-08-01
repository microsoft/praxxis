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

def test_import_ruleset_toml_duplicate_name(setup, rulesengine_root, rulesengine_db):
    from src.praxxis.rulesengine import import_ruleset
    from src.praxxis.sqlite import sqlite_rulesengine
    from tests.src.praxxis.util import dummy_object
    import os

    path_to_toml = os.path.join(os.path.dirname(__file__), "..",  "..", "..", "test_importables", "test_toml_ruleset.toml")

    sqlite_rulesengine.clear_ruleset_list(rulesengine_db)
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

def test_import_ruleset_does_not_exist(setup, rulesengine_root, rulesengine_db):
    from src.praxxis.rulesengine import import_ruleset
    from src.praxxis.sqlite import sqlite_rulesengine
    from src.praxxis.util import error
    from tests.src.praxxis.util import dummy_object
    from src.praxxis.display import display_error
    import os

    badpath1 = os.path.join(os.path.dirname(__file__), "..",  "..", "..", "test_importables", "noneexistent_file.toml")
    badpath2 = os.path.join(os.path.dirname(__file__), "..",  "..", "..", "test_notebooks", "test_notebook.ipynb")

    sqlite_rulesengine.clear_ruleset_list(rulesengine_db)
    assert sqlite_rulesengine.get_all_rulesets(rulesengine_db, 1, 100) == []

    name1 = dummy_object.make_dummy_path(badpath1)
    name2 = dummy_object.make_dummy_path(badpath2)
    
    try:
        import_ruleset.import_ruleset(name1, rulesengine_root, rulesengine_db)
        # if success:
        assert 0
    except error.NotValidRuleset as e:
        assert str(e) == display_error.invalid_ruleset_import(name1.path)
    
    try:
        import_ruleset.import_ruleset(name2, rulesengine_root, rulesengine_db)
        # if success:
        assert 0
    except error.NotValidRuleset as e:
        assert str(e) == display_error.invalid_ruleset_import(name2.path)
    
        
def test_import_database(setup, rulesengine_db, create_one_ruleset):
    from src.praxxis.rulesengine import import_ruleset
    from src.praxxis.sqlite import sqlite_rulesengine
    from tests.src.praxxis.util import dummy_object
    from src.praxxis.rulesengine import remove_ruleset

    name = "generated_one_ruleset"
    ruleset_path = sqlite_rulesengine.get_ruleset_path(rulesengine_db, name)

    name1 = dummy_object.make_dummy_ruleset(name, ruleset_path)

    sqlite_rulesengine.clear_ruleset_list(rulesengine_db)

    message = import_ruleset.import_ruleset(name1, name1.name, rulesengine_db)

    assert message == name1.name
    
    rulesets = sqlite_rulesengine.get_all_rulesets(rulesengine_db, query_start=1, end=5)

    assert len(rulesets) == 1
    assert len(rulesets[0]) == 2
    assert rulesets[0][0] == name1.name

    
    remove_ruleset.remove_ruleset(message, rulesengine_db)    
