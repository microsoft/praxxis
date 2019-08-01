"""
Marks a ruleset as activate 
(i.e., its rules will be evaluated when making predictions)
"""

def activate_ruleset(args, rulesengine_db):
    from src.praxxis.sqlite import sqlite_rulesengine
    from src.praxxis.display import display_rulesengine
    from src.praxxis.rulesengine import rules
    from src.praxxis.util import error

    if hasattr(args, "name"):
        name = args.name
    else:
        name = args

    name = rules.get_ruleset_by_ordinal(name, rulesengine_db)

    try:
        sqlite_rulesengine.activate_ruleset(rulesengine_db, name)
        display_rulesengine.display_activate_ruleset(name)
        return name
    except error.RulesetNotFoundError as e:
        raise e
    except error.RulesetActiveError as e:
        raise e