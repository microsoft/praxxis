"""
This file contains all the display functions for editing rules in a ruleset.
"""

def display_get_rule_name():
    """display function to prompt for the name of the rule to add""" 
    return input("Name of the rule to add: ")


def display_filename_input():
    """display function for inputting filenames""" 
    print("FILENAMES: The full or partial names of the files to apply this rule to.")
    print("To apply the rule without regard to filename, press enter without adding any filenames.")
    return input("Enter a comma-separated list of ordinals and/or strings: ")


def display_filenames(filenames):
    """display function for the filenames included in a rule""" 
    if filenames == ['']:
        print("This rule will predict for any output match regardless of filename")
    else:
        print("Strings this rule will check for in filenames: ")
        i = 1
        for filename in filenames:
            print("\t{i}.\t%s" %(filename))
            i += 1


def display_output_input():
    """display function that prompts for output strings to check for""" 
    print("\nOUTPUT: In any notebooks matching the filename(s) provided, the file output(s) that indicates this rule should be applied.")
    print("To apply the rule without regard to file output, press enter without adding any output strings.")
    return input("Enter output strings as a comma-separated list: ")


def display_outputs(outputs):
    """display function for the output strings that will trigger the rule"""
    if outputs == ['']:
        print("This rule will predict for any filename match regardless of output")
    else:
        print("Strings this rule will check for in file output: ")
        i = 1
        for output in outputs:
            print("\t%s.\t%s" %(i, output))
            i += 1


def display_predicted_notebooks_input():
    """display function for the notebooks to predict""" 
    print("\nPREDICTIONS: Type the ordinals of the notebooks to predict as next steps, in order")
    return input("Enter notebook ordinals as a comma-separated list: ")


def display_prediction_list(predictions):
    """display function for the list of predicted notebooks"""
    print("Predicted notebooks for this rule: ")
    i = 1
    for prediction in predictions:
        print("\t%s.\t%s" %(i, prediction))
        i += 1


def display_deletion_prompt():
    """display function for the prompt for which rule to delete"""
    return input("Enter the name or ordinal of the rule to delete: ")
