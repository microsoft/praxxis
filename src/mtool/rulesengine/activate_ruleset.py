
def activate_ruleset(args, prediction_db):
    from src.mtool.sqlite import sqlite_rulesengine
    from src.mtool.display import display_rulesengine
    from src.mtool.rulesengine import rules
    from src.mtool.util import error

    if hasattr(args, "name"):
        name = args.name
    else:
        name = args

    name = rules.get_ruleset_by_ordinal(name, prediction_db)

    try:
        sqlite_rulesengine.activate_ruleset(prediction_db, name)
        display_rulesengine.display_activate_ruleset(name)
    except error.RulesetNotFoundError as e:
        raise e
    except error.RulesetActiveError as e:
        raise e