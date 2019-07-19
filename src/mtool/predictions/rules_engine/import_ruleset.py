def import_ruleset(args, prediction_db):
    """links a ruleset db to the ruleset table"""
    from src.mtool.util.sqlite import sqlite_prediction
    from src.mtool.display import display_rulesengine
    import os
    
    path = args.path
    if not os.path.exists(path):
        from src.mtool.util.error import NotValidRuleset
        raise(NotValidRuleset(path))
    
    if(path.endswith(".db")):
        ruleset_name = os.path.basename(path).strip()[:-3]
        ruleset_root = path
        sqlite_prediction.add_ruleset_to_list(prediction_db, ruleset_name, ruleset_root)
        display_rulesengine.display_imported_ruleset(ruleset_name)
        """
        elif(path.endswith(".toml")):
            print("toml support here")
        """
    else:
        from src.mtool.util.error import NotValidRuleset
        raise(NotValidRuleset(path))
    
    