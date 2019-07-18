"""
Rules are defined as:

([filename match(es)],[output match(es)],[notebooks to suggest])

if either left-hand list is empty, this is interpreted as "all"
"""

def rules_check(prediction_db, filename, output_path, start, end):
    from src.mtool.util.sqlite import sqlite_prediction

    rulesets = sqlite_prediction.get_active_rulesets(prediction_db, start, end)

    rulesmatch = []
    hit = set()
    for ruleset in rulesets:
        filenames = sqlite_prediction.get_filenames_by_rule(ruleset[2])
        for fmatch in filenames:
            if fmatch[0] in filename:
                rulesmatch.append(fmatch[1])
 
        if rulesmatch != []:
            #get output
            from src.mtool.notebook.notebook import get_output_from_filename
            output = get_output_from_filename(output_path)
 
        outputs = sqlite_prediction.get_outputs_for_rules(ruleset[2], rulesmatch)
        for omatch in outputs:
            if omatch[0] in output:
                hit.add(omatch[1])
    sqlite_prediction.get_predictions(ruleset[2], hit)
            

    print(">>")
    print(hit)
    