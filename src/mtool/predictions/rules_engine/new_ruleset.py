
def new_ruleset(args, prediction_root, prediction_db):
    import os
    from src.mtool.util.sqlite import sqlite_prediction
    from src.mtool.display import display_prediction

    if hasattr(args, "name"):
        name = args.name
    else:
        name = args
        
    name = name.lower()

    if hasattr(args, "root"):
        root = args.root
    else:
        root = prediction_root
        
    path = os.path.join(root, f"{name}.db")

    if os.path.exists(path):
        i=1
        while os.path.exists(os.path.join(root, f"{name}-{i}.db")):
            i+= 1
        path = os.path.join(root, f"{name}-{i}.db")
        name = f"{name}-{i}"
    
    sqlite_prediction.init_ruleset(prediction_db, name, path)
    sqlite_prediction.add_ruleset_to_list(prediction_db, name, path)

    display_prediction.display_new_ruleset(name)
    return 

