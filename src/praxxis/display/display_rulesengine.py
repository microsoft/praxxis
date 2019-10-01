"""
This file contains all of the display functions for the rules engine
"""


def display_init_rulesengine_root(root):
    """display function for creating new rules engine folder"""
    print("Created rules engine directory at %s" %(root)) 


def display_init_rulesengine_db(db_root):
    """display function for initializing the rules engine db"""
    print("Created rules engine database at %s" %(db_root)) 


def display_new_ruleset(name):
    """display function for creating a new ruleset"""
    print("Created new ruleset \"%s\""  %(name))


def display_removed_ruleset(name):
    """display function for removing a ruleset"""
    print("Removed ruleset \"%s\"" %(name)) 


def display_activate_ruleset(name):
    """display function for activating a ruleset"""
    print("Ruleset \"%s\" is active" %(name)) 


def display_deactivate_ruleset(name):
    """display function for deactivating a ruleset"""
    print("Ruleset \"%s\" is no longer active" %(name)) 


def display_ruleset_list(rulesets):
    """display function for listing rulesets"""
    activation_messages = ["(INACTIVE)", "(ACTIVE)"]

    print("Rulesets:")
    i = 1
    for ruleset in rulesets:
        print("\t%s.\t%s\t\t%s" %(i, ruleset[0], activation_messages[ruleset[1]])) 
        i += 1


def display_rule_list(ruleset, rules):
    """display function for listing rules in a ruleset"""
    print("Rules in ruleset %s:" %(ruleset)) 

    i = 1
    for rule in rules:
        print("\t%s.\t%s" %(i, rule[0])) 
        i += 1


def display_rule(name, filenames, outputs, predictions):
    """display function for displaying a rule"""
    print("%s: %s %s = %s" %(name, filenames, outputs, [pred[2] for pred in predictions])) 


def display_added_rule(ruleset_name, name, filenames, outputs, predictions):
    """display function for adding a rule"""
    print("Added rule %s to %s:" %(name, ruleset_name)) 
    display_rule(name, filenames, outputs, predictions)


def display_rule_deletion(ruleset, rule):
    """display function for deleting a rule"""
    print("Rule %s successfully deleted from %s" %(rule, ruleset)) 


def display_predictions(predictions):
    """display function for displaying a list of predictions"""
    i = 1
    print("Predicted Notebooks: ")
    for nb in predictions:
        print("\t%s.\t%s" %(i, nb[0]))
        i += 1


def display_imported_ruleset(name):
    print("Ruleset %s imported successfully" %(name))
