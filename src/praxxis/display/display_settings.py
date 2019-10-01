"""
This file contains all the display functions for updating settings
"""


def display_opening_message():
    """display function for opening settings"""
    print("Welcome to the praxxis settings utility.")


def display_settings(settings, values):
    """display function for settings that can be modified"""
    print("Settings that can be modified:")
    i = 0
    for setting in settings:
        i += 1
        if(setting != "Password"):
            print("\t%s.\t%s = %s" %(i, setting, values.get(setting)))
        else:
            print("\t%s.\t%s" %(i, setting))


def display_menu_prompt():
    """display function for the menu prompt"""
    return input("Enter the ordinal of the setting to update (enter q to exit): ")


def display_value_prompt(setting, setting_help):
    """display function for setting a value"""
    print("\t>> %s: %s" %(setting, setting_help))
    if (setting != "Password"):
        return input("\t>> Enter a new value for %s: " %(setting))
    else:
        import getpass
        return getpass.getpass("\t>> Enter a new value for %s: " %(setting))


def display_value_updated(setting, changeVal):
    """display function for values updated"""
    if (setting != "Password"):
        print("\t>> setting changed: %s = %s\n" %(setting, changeVal))
    else:
        print("\t>> setting changed: %s\n" %(setting))
