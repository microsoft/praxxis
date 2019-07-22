
def deactivate_ruleset(args, prediction_db):
    from src.mtool.sqlite import sqlite_rulesengine
    from src.mtool.display import display_rulesengine
    from src.mtool.rulesengine import rules

    if hasattr(args, "name"):
        name = args.name
    else:
        name = args

    name = rules.get_ruleset_by_ordinal(name, prediction_db)

    sqlite_rulesengine.deactivate_ruleset(prediction_db, name)
    display_rulesengine.display_deactivate_ruleset(name)
    return name
