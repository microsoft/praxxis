"""
This file contains all of the display functions for parameters
"""

def display_delete_param(name):
    """ the display function for deleted parameters"""
    print("%s deleted" %(name)) 

    
def display_list_param(params):
    """the display function for listing parameters"""
    print("parameters: ")
    if params == []:
        print("\tNone Set")
        return
    i = 0
    for param in params:
        i += 1
        print("\t%s.\t%s = %s" %(i, param[0], param[1])) 


def display_set_param(name, value):
    """the display function for set parameters"""
    print("Set parameter for scene:\n\t%s = %s" %(name, value)) 


def display_view_param(params, set_params):
    """ the display function for viewing parameters"""
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
            print("\t%s.\t%s = " %(counter, name),  end="" ) 
            if name in set_params:
                print("%s%s"  %(Fore.BLUE, set_params[name]))
            else:
                print(params[name])
