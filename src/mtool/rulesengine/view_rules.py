"""
View a list of all rules in a ruleset
TODO: -v option to see rule definitions too
""" 
def view_rules(args, prediction_db):
    """view rules in a given ruleset"""
    from src.mtool.sqlite import sqlite_rulesengine
    from src.mtool.display import display_rulesengine
    from src.mtool.rulesengine import rules

    if hasattr(args, "name"):
        name = args.name
    else:
        name = args

       
    name = rules.get_ruleset_by_ordinal(name, prediction_db)

    ruleset_db = sqlite_rulesengine.get_ruleset_path(prediction_db, name)

    rules_list = sqlite_rulesengine.list_rules_in_ruleset(ruleset_db)
    display_rulesengine.display_rule_list(name, rules_list)
    return rules_list