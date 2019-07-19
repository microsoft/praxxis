
def activate_ruleset(args, prediction_db):
    from src.mtool.util.sqlite import sqlite_prediction
    from src.mtool.display import display_rulesengine
    from src.mtool.predictions.rules_engine import rules
    from src.mtool.util import error

    if hasattr(args, "name"):
        name = args.name
    else:
        name = args

    name = rules.get_ruleset_by_ordinal(name, prediction_db)

    try:
        sqlite_prediction.activate_ruleset(prediction_db, name)
        display_rulesengine.display_activate_ruleset(name)
    except error.RulesetNotFoundError as e:
        raise e
    except error.RulesetActiveError as e:
        raise e