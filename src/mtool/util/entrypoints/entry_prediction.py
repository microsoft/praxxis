from src.mtool.util.roots import _query_start
from src.mtool.util.roots import _query_end
from src.mtool.util.roots import _prediction_root
from src.mtool.util.roots import _prediction_db
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
                    prediction_root = _prediction_root,
                    prediction_db = _prediction_db
                    ):
    """calls the function to make a new ruleset"""
    from src.mtool.predictions.rules_engine import new_ruleset
    new_ruleset.new_ruleset(arg, prediction_root, prediction_db)
    return

def remove_ruleset(arg, 
                    prediction_root = _prediction_root,
                    prediction_db = _prediction_db
                    ):
    """calls the function to remove (delete) a ruleset"""
    from src.mtool.predictions.rules_engine import remove_ruleset
    remove_ruleset.remove_ruleset(arg, prediction_root, prediction_db)
    return

def list_rulesets(arg,
                    prediction_db = _prediction_db,
                    start = _query_start,
                    end = _query_end):
    """calls the function to list all rulesets"""
    from src.mtool.predictions.rules_engine import list_rulesets
    list_rulesets.list_rulesets(arg, prediction_db, start, end)
    return

def view_ruleset(arg, 
                    prediction_db = _prediction_db):
    """calls the function to view all rules in a ruleset"""
    from src.mtool.predictions.rules_engine import view_rules
    view_rules.view_rules(arg, prediction_db)
    return

def edit_ruleset(arg, 
                    prediction_db = _prediction_db,
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
        add_rule_to_ruleset(arg, prediction_db)
    elif arg.action == 'd':
        delete_rule_from_ruleset(arg, prediction_db)
    elif arg.action == 'm':
        modify_rule_in_ruleset(arg, prediction_db)
    return

def add_rule_to_ruleset(arg,
                    prediction_db = _prediction_db,
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

    from src.mtool.predictions.rules_engine import add_rule_to_ruleset
    add_rule_to_ruleset.add_rule_to_ruleset(arg, prediction_db, library_db, current_scene_db, start, end)

def delete_rule_from_ruleset(arg,
                    prediction_db = _prediction_db
                    ):
    from src.mtool.predictions.rules_engine import delete_rule_from_ruleset
    delete_rule_from_ruleset.delete_rule_from_ruleset(arg, prediction_db)

def modify_rule_in_ruleset(arg,
                    prediction_db = _prediction_db
                    ):
    print("M")

def import_ruleset(arg):
    print("ir")
    return

def activate_ruleset(arg,
                    prediction_db = _prediction_db
                    ):
    from src.mtool.predictions.rules_engine import activate_ruleset
    activate_ruleset.activate_ruleset(arg, prediction_db)
    return

def deactivate_ruleset(arg,
                    prediction_db = _prediction_db
                    ):
    from src.mtool.predictions.rules_engine import deactivate_ruleset
    deactivate_ruleset.deactivate_ruleset(arg, prediction_db)
    return

def update_model(arg):
    print("um:")
    return

def init_prediction(prediction_root, prediction_db):
    import os
    
    from src.mtool.display import display_prediction
    from src.mtool.util.sqlite import sqlite_prediction

    os.mkdir(prediction_root)
    display_prediction.display_init_prediction_root(prediction_root)
    sqlite_prediction.init_prediction_db(prediction_db)
    display_prediction.display_init_prediction_db(prediction_db)
    return

