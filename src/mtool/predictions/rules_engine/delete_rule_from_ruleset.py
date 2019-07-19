
def delete_rule_from_ruleset(args, prediction_db):
    from src.mtool.util.sqlite import sqlite_rulesengine
    from src.mtool.display import display_rulesengine
    from src.mtool.display import display_edit_ruleset
    from src.mtool.predictions.rules_engine import rules

    if hasattr(args, "name"):
        name = args.name
    else:
        name = args

    name = rules.get_ruleset_by_ordinal(name, prediction_db)

    ruleset_db = sqlite_rulesengine.get_ruleset_path(prediction_db, name)

    rules_list = sqlite_rulesengine.list_rules_in_ruleset(ruleset_db)

    display_rulesengine.display_rule_list(name, rules_list)

    deletion = display_edit_ruleset.display_deletion_prompt()

    deletion_name = get_rule_by_ordinal(deletion, rules_list)

    sqlite_rulesengine.delete_rule(ruleset_db, deletion_name)
    
    display_rulesengine.display_rule_deletion(name, deletion_name)

def get_rule_by_ordinal(name, ruleslist):
    """gets rule by ordinal using a list of tuples"""
    from src.mtool.util.sqlite import sqlite_rulesengine
    from src.mtool.util import error

    if f"{name}".isdigit():
        try:
            name = ruleslist[int(name)-1][0]
        except IndexError:
            raise error.RuleNotFoundError(name)
    else:
        ruleslist = [rule[0] for rule in ruleslist] # un-tuple the list to check if name valid
        if name not in ruleslist:
            raise error.RuleNotFoundError(name)
    return(name)