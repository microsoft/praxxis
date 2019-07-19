"""
This file contains all of the display functions for parameters
"""

def display_delete_param(name):
    """ the display function for deleted parameters"""
    print(f"{name} deleted")

    
def display_list_param(params):
    """the display function for listing parameters"""
    print(f"parameter Variables: ")
    if params == []:
        print("\tNone Set")
        return
    i = 0
    for param in params:
        i += 1
        print(f"\t{i}.\t{param[0]} = {param[1]}")


def display_set_param(name, value):
    """the display function for set parameters"""
    print(f"Set parameter for scene:\n\t{name} = {value}")


def display_view_param(params, set_params):
    from colorama import init, Fore, Style
    init()
    if params == []:
        print("No parameters")
    else:
        set_params = dict(set_params)
        params = dict(params)
        counter = 0
        for name in params:
            counter += 1
            print(f"\t{counter}.\t{name} = ", end="")
            if name in set_params:
                print(f"{Fore.BLUE}{set_params[name]}{Style.RESET_ALL}" )
            else:
                print(params[name])
