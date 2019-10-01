"""
This file imports a ruleset.
"""

from src.praxxis.sqlite import sqlite_rulesengine
from src.praxxis.display import display_rulesengine


def import_ruleset(args, ruleset_root, rulesengine_db):
    """links a ruleset db to the ruleset table"""
    import os
    
    path = args.path
    if not os.path.exists(path):
        from src.praxxis.util.error import NotValidRuleset
        raise(NotValidRuleset(path))
    
    if(path.endswith(".db")):
        ruleset_name = os.path.basename(path).strip()[:-3]
        ruleset_root = path
        sqlite_rulesengine.add_ruleset_to_list(rulesengine_db, ruleset_name, ruleset_root)
        display_rulesengine.display_imported_ruleset(ruleset_name)    
    elif(path.endswith(".toml")):
        ruleset_name = parse_toml(path, ruleset_root, rulesengine_db)
    else:
        from src.praxxis.util.error import NotValidRuleset
        raise(NotValidRuleset(path))
    
    return ruleset_name


def parse_toml(path, ruleset_root, rulesengine_db):
    """parses a toml file into a ruleset"""
    import toml
    import os
    rulesetInfo = toml.load(path)

    ruleset_name = os.path.basename(path)[:-5]
    ruleset_db = os.path.join(ruleset_root, ruleset_name + ".db")
    i = 0
    while os.path.exists(ruleset_db):
        i += 1
        ruleset_db = os.path.join(ruleset_root, "%s-%s.db" %(ruleset_name, i))
    if i != 0:
        ruleset_name = "%s-%s" %(ruleset_name, i)

    sqlite_rulesengine.init_ruleset(rulesengine_db, ruleset_name, ruleset_db)
    sqlite_rulesengine.add_ruleset_to_list(rulesengine_db, ruleset_name, ruleset_db)

    for rulename in rulesetInfo:
        try:
            filenames = rulesetInfo[rulename]["filenames"]
            outputs = rulesetInfo[rulename]["outputs"]
            predictions_raw = rulesetInfo[rulename]["predictions"]
            pos = 1
            predictions = []
            for prediction in predictions_raw:
                if len(prediction) == 2: # no rawURL specified
                    prediction.append(None)
                predictions.append((rulename, pos, *prediction))
                pos += 1
                
            sqlite_rulesengine.add_rule(ruleset_db, rulename, filenames, outputs, predictions)
            display_rulesengine.display_added_rule(ruleset_name, rulename, filenames, outputs, predictions)
        except KeyError:
            from src.praxxis.display import display_error
            display_error.invalid_rule_definition(rulename)

    return ruleset_name
