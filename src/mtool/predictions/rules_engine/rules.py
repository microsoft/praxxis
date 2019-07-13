"""utilities for rules engine operation"""

def get_ruleset_by_ordinal(name, prediction_db):
    """gets ruleset by ordinal using the sqlite prediction db"""
    from src.mtool.util.sqlite import sqlite_prediction
    from src.mtool.util import error

    if f"{name}".isdigit():
        try:
            name = sqlite_prediction.get_ruleset_by_ord(prediction_db, int(name))
        except error.RulesetNotFoundError as e:
            raise e
    else:
        return(name)