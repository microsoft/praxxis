"""utilities for rules engine operation"""

def get_ruleset_by_ordinal(name, rulesengine_db):
    """gets ruleset by ordinal using the sqlite prediction db"""
    from src.praxxis.sqlite import sqlite_rulesengine
    from src.praxxis.util import error

    if f"{name}".isdigit():
        try:
            name = sqlite_rulesengine.get_ruleset_by_ord(rulesengine_db, int(name))
        except error.RulesetNotFoundError as e:
            raise e
    return(name)