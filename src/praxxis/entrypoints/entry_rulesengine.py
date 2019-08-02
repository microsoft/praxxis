"""
handles rules engine functions from the CLI
"""
from src.praxxis.util.roots import _query_start
from src.praxxis.util.roots import _query_end
from src.praxxis.util.roots import _rulesengine_root
from src.praxxis.util.roots import _rulesengine_db
from src.praxxis.util.roots import _library_db
from src.praxxis.util.roots import _scene_root
from src.praxxis.util.roots import _history_db
from src.praxxis.util.roots import _query_start
from src.praxxis.util.roots import _query_end


def new_ruleset(arg, 
                    rulesengine_root = _rulesengine_root,
                    rulesengine_db = _rulesengine_db
                    ):
    """calls the function to make a new ruleset"""
    from src.praxxis.rulesengine import new_ruleset
    new_ruleset.new_ruleset(arg, rulesengine_root, rulesengine_db)
    return


def remove_ruleset(arg, 
                    rulesengine_db = _rulesengine_db
                    ):
    """calls the function to remove (delete) a ruleset"""
    from src.praxxis.rulesengine import remove_ruleset
    remove_ruleset.remove_ruleset(arg, rulesengine_db)
    return


def list_rulesets(arg,
                    rulesengine_db = _rulesengine_db,
                    query_start = _query_start,
                    query_end = _query_end):
    """calls the function to list all rulesets"""
    from src.praxxis.rulesengine import list_rulesets
    list_rulesets.list_rulesets(arg, rulesengine_db, query_start, query_end)
    return


def view_ruleset(arg, 
                    rulesengine_db = _rulesengine_db):
    """calls the function to view all rules in a ruleset"""
    from src.praxxis.rulesengine import view_rules
    view_rules.view_rules(arg, rulesengine_db)
    return


def edit_ruleset(arg, 
                    rulesengine_db = _rulesengine_db,
                    library_db = _library_db, 
                    current_scene_db = None,
                    scene_root = _scene_root,
                    history_db = _history_db,
                    query_start = _query_start,
                    query_end = _query_end):
    """calls the function to the edit the ruleset"""
    from src.praxxis.util import roots
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
                    query_start = _query_start,
                    query_end = _query_end):
    """calls the function to add a rule to a ruleset"""
    from src.praxxis.util import roots
    if current_scene_db == None:
        current_scene_db = roots.get_current_scene_db(scene_root, history_db)

    from src.praxxis.rulesengine import add_rule_to_ruleset
    add_rule_to_ruleset.add_rule_to_ruleset(arg, rulesengine_db, library_db, current_scene_db, query_start, query_end)


def delete_rule_from_ruleset(arg,
                             rulesengine_db = _rulesengine_db):
    """calls the function to delete a rule from a ruleset"""
    from src.praxxis.rulesengine import delete_rule_from_ruleset

    delete_rule_from_ruleset.delete_rule_from_ruleset(arg, rulesengine_db)


def modify_rule_in_ruleset(arg,
                           rulesengine_db = _rulesengine_db):
    """modifies a rule defined in a ruleset"""
    print("M")


def import_ruleset(arg,
                    rulesengine_root = _rulesengine_root,
                    rulesengine_db = _rulesengine_db):
    """calls the function to import a ruleset"""
    from src.praxxis.rulesengine import import_ruleset
    
    import_ruleset.import_ruleset(arg, rulesengine_root, rulesengine_db)
    return


def activate_ruleset(arg,
                    rulesengine_db = _rulesengine_db):
    """calls the function to activate a ruleset"""
    from src.praxxis.rulesengine import activate_ruleset

    activate_ruleset.activate_ruleset(arg, rulesengine_db)
    return


def deactivate_ruleset(arg,
                    rulesengine_db = _rulesengine_db):
    """calls the function to deactivate a ruleset"""
    from src.praxxis.rulesengine import deactivate_ruleset

    deactivate_ruleset.deactivate_ruleset(arg, rulesengine_db)
    return


def init_rulesengine(rulesengine_root, rulesengine_db):
    """initializes the ruleset db and directory"""
    import os
    
    from src.praxxis.display import display_rulesengine
    from src.praxxis.sqlite import sqlite_init

    os.mkdir(rulesengine_root)
    display_rulesengine.display_init_rulesengine_root(rulesengine_root)
    sqlite_init.init_rulesengine_db(rulesengine_db)
    display_rulesengine.display_init_rulesengine_db(rulesengine_db)
    return
