"""
View a list of all rules in a ruleset
TODO: -v option to see rule definitions too
""" 


def view_rules(args, rulesengine_db):
    """view rules in a given ruleset"""
    from src.praxxis.sqlite import sqlite_rulesengine
    from src.praxxis.display import display_rulesengine
    from src.praxxis.rulesengine import rules

    if hasattr(args, "name"):
        name = args.name
    else:
        name = args

       
    name = rules.get_ruleset_by_ordinal(name, rulesengine_db)

    ruleset_db = sqlite_rulesengine.get_ruleset_path(rulesengine_db, name)

    rules_list = sqlite_rulesengine.list_rules_in_ruleset(ruleset_db)
    display_rulesengine.display_rule_list(name, rules_list)

    return rules_list
