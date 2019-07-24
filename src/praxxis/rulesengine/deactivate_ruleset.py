"""
Deactivates a ruleset.
(i.e., the ruleset remains on disk but will not be used in making predictions)
"""

def deactivate_ruleset(args, prediction_db):
    from src.praxxis.sqlite import sqlite_rulesengine
    from src.praxxis.display import display_rulesengine
    from src.praxxis.rulesengine import rules

    if hasattr(args, "name"):
        name = args.name
    else:
        name = args

    name = rules.get_ruleset_by_ordinal(name, prediction_db)

    sqlite_rulesengine.deactivate_ruleset(prediction_db, name)
    display_rulesengine.display_deactivate_ruleset(name)
    return name
