from src.mtool.util.roots import _query_start
from src.mtool.util.roots import _query_end
from src.mtool.util.roots import _prediction_root
from src.mtool.util.roots import _prediction_db

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
    from src.mtool.predictions.rules_engine import remove_ruleset
    remove_ruleset.remove_ruleset(arg, prediction_root, prediction_db)
    return

def list_rulesets(arg,
                    prediction_db = _prediction_db):
    from src.mtool.predictions.rules_engine import list_rulesets
    list_rulesets.list_rulesets(arg, prediction_db)
    return

def view_ruleset(arg):
    print("vr")
    return

def edit_ruleset(arg):
    print("er")
    return

def import_ruleset(arg):
    print("ir")
    return

def activate_ruleset(arg):
    print("ars")
    return

def deactivate_ruleset(arg):
    print("drs")
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