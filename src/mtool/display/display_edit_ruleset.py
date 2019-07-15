"""
This file contains all the display functions for editing rules in a ruleset.
"""

def display_get_rule_name():
    return input("Name of the rule to add: ")

def display_filename_input():
    print("FILENAMES: The full or partial names of the files to apply this rule to.")
    return input("Enter a comma-separated list of ordinals and/or strings")