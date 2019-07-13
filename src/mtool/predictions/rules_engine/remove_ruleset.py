def remove_ruleset(args, prediction_root, prediction_db):
    import os
    from src.mtool.util.sqlite import sqlite_prediction

    print("Swarathmika")

    path = sqlite_prediction.get_ruleset_path(prediction_db, args.name)

    os.remove(path[0])

