
from src.mtool.sqlite import sqlite_init
from src.mtool.sqlite import sqlite_rulesengine
from src.mtool.display import display_rulesengine

def import_ruleset(args, ruleset_root, rulesengine_db):
    """links a ruleset db to the ruleset table"""
    from src.mtool.sqlite import sqlite_rulesengine
    from src.mtool.display import display_rulesengine
    import os
    
    path = args.path
    if not os.path.exists(path):
        from src.mtool.util.error import NotValidRuleset
        raise(NotValidRuleset(path))
    
    if(path.endswith(".db")):
        ruleset_name = os.path.basename(path).strip()[:-3]
        ruleset_root = path
        sqlite_rulesengine.add_ruleset_to_list(rulesengine_db, ruleset_name, ruleset_root)
        display_rulesengine.display_imported_ruleset(ruleset_name)    
    elif(path.endswith(".toml")):
        parse_toml(path, ruleset_root, rulesengine_db)
    else:
        from src.mtool.util.error import NotValidRuleset
        raise(NotValidRuleset(path))
    
def parse_toml(path, ruleset_root, rulesengine_db):
    import toml
    import os
    rulesetInfo = toml.load(path)

    ruleset_name = os.path.basename(path)[:-5]
    ruleset_db = os.path.join(ruleset_root, ruleset_name + ".db")
    sqlite_init.init_ruleset(rulesengine_db, ruleset_name, ruleset_db)

    for rulename in rulesetInfo:
        try:
            filenames = rulesetInfo[rulename]["filenames"]
            outputs = rulesetInfo[rulename]["outputs"]
            predictions = rulesetInfo[rulename]["predictions"]
            print(predictions)
            sqlite_rulesengine.add_rule(ruleset_db, rulename, filenames, outputs, predictions)
            display_rulesengine.display_added_rule(ruleset_name, rulename, filenames, outputs, predictions)
        except KeyError:
            from src.mtool.display import display_error
            display_error.invalid_rule_definition(rulename)

    
    
    