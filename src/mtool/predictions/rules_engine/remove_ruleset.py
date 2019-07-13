
def remove_ruleset(args, prediction_root, prediction_db):
    import os
    from src.mtool.util.sqlite import sqlite_prediction
    from src.mtool.predictions.rules_engine import rules

    name = rules.get_ruleset_by_ordinal(args.name, prediction_db)

    path = sqlite_prediction.get_ruleset_path(prediction_db, name)
    os.remove(path)

    sqlite_prediction.remove_ruleset(prediction_db, name)

    return

