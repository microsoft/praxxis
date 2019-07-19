
def remove_ruleset(args, rulesengine_db):
    import os
    from src.mtool.sqlite import sqlite_rulesengine
    from src.mtool.rulesengine import rules

    if hasattr(args, "name"):
        name = args.name
    else:
        name = args

    name = rules.get_ruleset_by_ordinal(name, rulesengine_db)

    path = sqlite_rulesengine.get_ruleset_path(rulesengine_db, name)
    os.remove(path)

    sqlite_rulesengine.remove_ruleset(rulesengine_db, name)

    return

