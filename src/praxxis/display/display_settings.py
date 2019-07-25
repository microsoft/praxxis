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
            print(f'\t{i}.\t{setting} = {values.get(setting)}')
        else:
            print(f'\t{i}.\t{setting}')


def display_menu_prompt():
    """ display function for the menu prompt"""
    return input("Enter the ordinal of the setting to update (enter q to exit): ")


def display_value_prompt(setting, setting_help):
    """ display function for setting a value"""
    print(f"\t>> {setting}: {setting_help}")
    if (setting != "Password"):
        return input(f"\t>> Enter a new value for {setting}: ")
    else:
        import getpass
        return getpass.getpass(f"\t>> Enter a new value for {setting}: ")


def display_value_updated(setting, changeVal):
    """display function for values updated"""
    if (setting != "Password"):
        print(f"\t>> setting changed: {setting} = {changeVal}\n")
    else:
        print(f"\t>> setting changed: {setting}\n")
    