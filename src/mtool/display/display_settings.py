"""
This file contains all the display functions for updating settings
"""

def display_opening_message():
    print("Welcome to the mtool settings utility.")

def display_settings(settings, curr_values):
    print("Settings that can be modified:")
    for i in range(len(settings)):
        if(settings[i] != "Password"):
            print(f'\t{i+1}.\t{settings[i]} = {curr_values[i]}')
        else:
            print(f'\t{i+1}.\t{settings[i]}')

def display_menu_prompt():
    return input("Enter the ordinal of the setting to update (enter '0' or 'exit' to exit): ")

def display_value_prompt(setting):
    return input(f"Enter a new value for {setting}: ")

def display_value_updated(setting, changeVal):
    print(f"\tsuccess! set {setting} = {changeVal}\n")