
def remove_ruleset(args, prediction_root, prediction_db):
    import os
    from src.mtool.util.sqlite import sqlite_prediction
    from src.mtool.predictions.rules_engine import rules

    if hasattr(args, "name"):
        name = args.name
    else:
        name = args

    name = rules.get_ruleset_by_ordinal(name, prediction_db)

    path = sqlite_prediction.get_ruleset_path(prediction_db, name)
    os.remove(path)

    sqlite_prediction.remove_ruleset(prediction_db, name)

    return

