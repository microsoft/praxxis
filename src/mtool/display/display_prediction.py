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
