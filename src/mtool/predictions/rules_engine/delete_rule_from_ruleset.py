
def delete_rule_from_ruleset(args, prediction_db):
    from src.mtool.util.sqlite import sqlite_prediction
    from src.mtool.display import display_prediction
    from src.mtool.display import display_edit_ruleset
    from src.mtool.predictions.rules_engine import rules

    if hasattr(args, "name"):
        name = args.name
    else:
        name = args

    name = rules.get_ruleset_by_ordinal(name, prediction_db)

    ruleset_db = sqlite_prediction.get_ruleset_path(prediction_db, name)

    rules = sqlite_prediction.list_rules_in_ruleset(ruleset_db)

    display_prediction.display_rule_list(name, rules)

    deletion = display_edit_ruleset.display_deletion_prompt()


    for rule in rules:
        print(rule[0])