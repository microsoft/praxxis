
def deactivate_ruleset(args, prediction_db):
    from src.mtool.util.sqlite import sqlite_prediction
    from src.mtool.display import display_prediction
    from src.mtool.predictions.rules_engine import rules

    if hasattr(args, "name"):
        name = args.name
    else:
        name = args

    name = rules.get_ruleset_by_ordinal(name, prediction_db)

    sqlite_prediction.deactivate_ruleset(prediction_db, name)
    display_prediction.display_deactivate_ruleset(name)