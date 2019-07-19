"""
This file lists all rulesets by name
"""

def list_rulesets(args, prediction_db, start, end):
    """lists all rulesets and whether each is currently activated"""
    from src.mtool.util.sqlite import sqlite_rulesengine
    from src.mtool.display import display_rulesengine

    result = sqlite_rulesengine.get_all_rulesets(prediction_db, start, end)
    display_rulesengine.display_ruleset_list(result)
