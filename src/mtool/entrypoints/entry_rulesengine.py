from src.mtool.util.roots import _query_start
from src.mtool.util.roots import _query_end
from src.mtool.util.roots import _rulesengine_root
from src.mtool.util.roots import _rulesengine_db
from src.mtool.util.roots import _library_db
from src.mtool.util.roots import _scene_root
from src.mtool.util.roots import _history_db
from src.mtool.util.roots import _query_start
from src.mtool.util.roots import _query_end

"""
TODO: testing ;)
TODO: edit ruleset
"""

def new_ruleset(arg, 
                    rulesengine_root = _rulesengine_root,
                    rulesengine_db = _rulesengine_db
                    ):
    """calls the function to make a new ruleset"""
    from src.mtool.rulesengine import new_ruleset
    new_ruleset.new_ruleset(arg, rulesengine_root, rulesengine_db)
    return

def remove_ruleset(arg, 
                    rulesengine_db = _rulesengine_db
                    ):
    """calls the function to remove (delete) a ruleset"""
    from src.mtool.rulesengine import remove_ruleset
    remove_ruleset.remove_ruleset(arg, rulesengine_db)
    return

def list_rulesets(arg,
                    rulesengine_db = _rulesengine_db,
                    start = _query_start,
                    end = _query_end):
    """calls the function to list all rulesets"""
    from src.mtool.rulesengine import list_rulesets
    list_rulesets.list_rulesets(arg, rulesengine_db, start, end)
    return

def view_ruleset(arg, 
                    rulesengine_db = _rulesengine_db):
    """calls the function to view all rules in a ruleset"""
    from src.mtool.rulesengine import view_rules
    view_rules.view_rules(arg, rulesengine_db)
    return

def edit_ruleset(arg, 
                    rulesengine_db = _rulesengine_db,
                    library_db = _library_db, 
                    current_scene_db = None,
                    scene_root = _scene_root,
                    history_db = _history_db,
                    start = _query_start,
                    end = _query_end):
    from src.mtool.util import roots
    if current_scene_db == None:
        current_scene_db = roots.get_current_scene_db(scene_root, history_db)

    if arg.action == 'a':
        add_rule_to_ruleset(arg, rulesengine_db)
    elif arg.action == 'd':
        delete_rule_from_ruleset(arg, rulesengine_db)
    elif arg.action == 'm':
        modify_rule_in_ruleset(arg, rulesengine_db)
    return

def add_rule_to_ruleset(arg,
                    rulesengine_db = _rulesengine_db,
                    library_db = _library_db, 
                    current_scene_db = None,
                    scene_root = _scene_root,
                    history_db = _history_db,
                    start = _query_start,
                    end = _query_end
                    ):
    from src.mtool.util import roots
    if current_scene_db == None:
        current_scene_db = roots.get_current_scene_db(scene_root, history_db)

    from src.mtool.rulesengine import add_rule_to_ruleset
    add_rule_to_ruleset.add_rule_to_ruleset(arg, rulesengine_db, library_db, current_scene_db, start, end)

def delete_rule_from_ruleset(arg,
                    rulesengine_db = _rulesengine_db
                    ):
    from src.mtool.rulesengine import delete_rule_from_ruleset
    delete_rule_from_ruleset.delete_rule_from_ruleset(arg, rulesengine_db)

def modify_rule_in_ruleset(arg,
                    rulesengine_db = _rulesengine_db
                    ):
    print("M")

def import_ruleset(arg,
                    rulesengine_db = _rulesengine_db):
    from src.mtool.rulesengine import import_ruleset
    import_ruleset.import_ruleset(arg, rulesengine_db)
    return

def activate_ruleset(arg,
                    rulesengine_db = _rulesengine_db
                    ):
    from src.mtool.rulesengine import activate_ruleset
    activate_ruleset.activate_ruleset(arg, rulesengine_db)
    return

def deactivate_ruleset(arg,
                    rulesengine_db = _rulesengine_db
                    ):
    from src.mtool.rulesengine import deactivate_ruleset
    deactivate_ruleset.deactivate_ruleset(arg, rulesengine_db)
    return

def init_rulesengine(rulesengine_root, rulesengine_db):
    import os
    
    from src.mtool.display import display_rulesengine
    from src.mtool.sqlite import sqlite_init

    os.mkdir(rulesengine_root)
    display_rulesengine.display_init_rulesengine_root(rulesengine_root)
    sqlite_init.init_rulesengine_db(rulesengine_db)
    display_rulesengine.display_init_rulesengine_db(rulesengine_db)
    return

