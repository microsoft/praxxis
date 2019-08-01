"""
This file lists all rulesets by name
"""

def list_rulesets(args, rulesengine_db, query_start, query_end):
    """lists all rulesets and whether each is currently activated"""
    from src.praxxis.sqlite import sqlite_rulesengine
    from src.praxxis.display import display_rulesengine

    result = sqlite_rulesengine.get_all_rulesets(rulesengine_db, query_start, query_end)
    display_rulesengine.display_ruleset_list(result)
    
    return result
