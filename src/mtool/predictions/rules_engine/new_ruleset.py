
def new_ruleset(args, prediction_root, prediction_db):
    import os
    from src.mtool.util.sqlite import sqlite_prediction

    if hasattr(args, "name"):
        name = args.name
    else:
        name = args
        
    name = f"{name.lower()}.db"

    if hasattr(args, "root"):
        root = args.root
    else:
        root = prediction_root
    
    path = os.path.join(root, name)

    sqlite_prediction.init_ruleset(prediction_db, name, path)

    return 

