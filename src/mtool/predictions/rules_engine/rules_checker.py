"""
Rules are defined as:

([filename match(es)],[output match(es)],[notebooks to suggest])

if either left-hand list is empty, this is interpreted as "all"
"""

def rules_check(prediction_db, filename, output, start, end):
    from src.mtool.util.sqlite import sqlite_prediction

    rulesets = sqlite_prediction.get_active_rulesets(prediction_db, start, end)
    print(rulesets)

    for ruleset in rulesets:
        rules = sqlite_prediction.list_rules_in_ruleset(ruleset[1])
        print(rules)
        for rule in rules:
            filenames = sqlite_prediction.get_filenames(ruleset[1], rule)
            print(filenames)