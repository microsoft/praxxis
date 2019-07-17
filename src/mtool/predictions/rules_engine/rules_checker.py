"""
Rules are defined as:

([filename match(es)],[output match(es)],[notebooks to suggest])

if either left-hand list is empty, this is interpreted as "all"
"""

def rules_check(prediction_db, filename, output, start, end):
    from src.mtool.util.sqlite import sqlite_prediction

    rulesets = sqlite_prediction.get_active_rulesets(prediction_db, start, end)

    rulesmatch = []
    hit = []
    for ruleset in rulesets:
        rules = sqlite_prediction.list_rules_in_ruleset(ruleset[2])
        for rule in rules:
            filenames = sqlite_prediction.get_filenames(ruleset[2], rule[0])
            for fmatch in filenames:
                if fmatch[0] in filename:
                    rulesmatch.append(rule[0])

        if rulesmatch != []:
            #get output
            pass
            
        for rule in rulesmatch:
            outputs = sqlite_prediction.get_outputs(ruleset[2], rule)
            for omatch in outputs:
                if omatch[0] in output:
                    hit.append(rule)
            
        print(hit)