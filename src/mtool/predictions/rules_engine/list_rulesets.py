"""
This file lists all rulesets by name
"""

def list_rulesets(args, prediction_db):
    """lists all rulesets and whether each is currently activated"""
    from src.mtool.util.sqlite import sqlite_prediction
    from src.mtool.display import display_prediction

    result = sqlite_prediction.get_all_rulesets(prediction_db, start=0, end=100)
    display_prediction.display_ruleset_list(result)
