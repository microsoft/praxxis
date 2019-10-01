"""
This file completely deletes a ruleset.
"""


def remove_ruleset(args, rulesengine_db):
    """remove a ruleset, deleting the associated db"""
    import os
    from src.praxxis.sqlite import sqlite_rulesengine
    from src.praxxis.rulesengine import rules

    if hasattr(args, "name"):
        name = args.name
    else:
        name = args

    name = rules.get_ruleset_by_ordinal(name, rulesengine_db)

    path = sqlite_rulesengine.get_ruleset_path(rulesengine_db, name)

    if os.path.isfile(path):
        os.remove(path)
        sqlite_rulesengine.remove_ruleset(rulesengine_db, name)
    else:
        from src.praxxis.util import error
        raise error.RulesetNotFoundError(name)

    return name
