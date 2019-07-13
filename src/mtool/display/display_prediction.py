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