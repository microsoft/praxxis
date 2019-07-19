"""
This file contains all of the display functions for predictions
"""

def display_init_prediction_root(root):
    """the display function for creating new prediction folder"""
    print(f"Created predictions directory at {root}")

def display_init_prediction_db(db_root):
    """the display function for initializing the prediction db"""
    print(f"Created predictions database at {db_root}")

def display_new_ruleset(name):
    """the display function for creating a new ruleset"""
    print(f"Created new ruleset \"{name}\"")

def display_removed_ruleset(name):
    """the display function for removing a ruleset"""
    print(f"Removed ruleset \"{name}\"")

def display_activate_ruleset(name):
    """the display function for activating a ruleset"""
    print(f"Ruleset \"{name}\" is active")

def display_deactivate_ruleset(name):
    """the display function for deactivating a ruleset"""
    print(f"Ruleset \"{name}\" is no longer active")

def display_ruleset_list(rulesets):
    """the display function for listing rulesets"""
    activation_messages = ["(INACTIVE)", "(ACTIVE)"]

    print("Rulesets:")

    i = 1
    for ruleset in rulesets:
        print(f'\t{i}.\t{ruleset[0]}\t\t{activation_messages[ruleset[1]]}')
        i += 1

def display_rule_list(ruleset, rules):
    """the display function for listing rules in a ruleset"""
    print(f"Rules in ruleset {ruleset}:")

    i = 1
    for rule in rules:
        print(f'\t{i}.\t{rule[0]}')
        i += 1

def display_rule(name, filenames, outputs, predictions):
    print(f"{name}: {filenames} {outputs} = {predictions}")


def display_rule_deletion(ruleset, rule):
    """the display function for deleting a rule"""
    print(f"Rule {rule} successfully deleted from {ruleset}")

def display_predictions(predictions):
    """the display function for displaying a list of predictions"""
    i = 1
    print("Predicted Notebooks: ")
    for nb in predictions:
        print(f'\t{i}.\t{nb[0]}')
        i += 1

def display_imported_ruleset(name):
    print(f"Ruleset {name} imported successfully")