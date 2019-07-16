"""
This file contains all the display functions for editing rules in a ruleset.
"""

def display_get_rule_name():
    return input("Name of the rule to add: ")

def display_filename_input():
    print("FILENAMES: The full or partial names of the files to apply this rule to.")
    print("To apply the rule without regard to filename, press enter without adding any filenames.")
    return input("Enter a comma-separated list of ordinals and/or strings: ")

def display_filenames(filenames):
    if filenames == ['']:
        print("This rule will predict for any output match regardless of filename")
    else:
        print("Strings this rule will check for in filenames: ")
        i = 1
        for filename in filenames:
            print(f"\t{i}.\t{filename}")
            i += 1

def display_output_input():
    print("\nOUTPUT: In any notebooks matching the filename(s) provided, the file output(s) that indicates this rule should be applied.")
    print("To apply the rule without regard to file output, press enter without adding any output strings.")
    return input("Enter output strings as a comma-separated list: ")

def display_outputs(outputs):
    if outputs == ['']:
        print("This rule will predict for any filename match regardless of output")
    else:
        print("Strings this rule will check for in file output: ")
        i = 1
        for output in outputs:
            print(f"\t{i}.\t{output}")
            i += 1

def display_predicted_notebooks_input():
    print("\nPREDICTIONS: Type the ordinals of the notebooks to predict as next steps, in order")
    return input("Enter notebook ordinals as a comma-separated list: ")

def display_rule(name, filenames, outputs, predictions):
    print(f"{name}: {filenames} {outputs} = {predictions}")

def display_predictions(predictions):
    print("Predicted notebooks for this rule: ")
    i = 1
    for prediction in predictions:
        print(f"\t{i}.\t{prediction}")
        i += 1

def display_deletion_prompt():
    return input("Enter the name or ordinal of the rule to delete: ")