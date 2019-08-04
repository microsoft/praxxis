"""
This file contains all of the error messages
"""

# this allows for the error messages to be colored.
# autoreset=True resets the color after every print
from colorama import init, Fore, Style
init(autoreset=True, convert=True)

def param_not_found_error(name):
    """error display for parameters not being found"""
    return("%sparameter %s not found" %(Fore.RED, name)) 


def notebook_load_error(name):
    """error display for a notebook failing to load"""
    print("\t%sthere is something wrong with %s. praxxis will still load it, but it might not run." %(Fore.RED, name)) 


def scene_not_found_error(name):
    """error display for scenes not existing"""
    if name == None:
        return("%sscene does not exist" %(Fore.RED))  
    else:
        return("%sscene %s does not exist"  %(Fore.RED, name))


def notebook_not_found_error(name):
    """error display for notebooks not existing"""
    if name == None:
        return("%snotebook does not exist" %(name))
    else:
        return("%snotebook %s does not exist" %(Fore.RED, name))


def rule_not_found_error(name):
    """error display for a rule not existing"""
    if name == None:
        return("%srule does not exist" %(name))
    else:
        return("%srule %s does not exist" %(Fore.RED, name))


def ruleset_not_found_error(name):
    """error display for a ruleset not existing"""
    if name == None:
        return("%sruleset does not exist" %(name)) 
    else:
        return("%sruleset %s does not exist" %(Fore.RED, name)) 


def ruleset_active_error(name):
    """error display for activating an active ruleset"""
    if name == None:
        return("%sruleset is already active" %(name))
    else:
        return("%sruleset %s is already active" %(Fore.RED, name)) 


def ruleset_not_active_error(name):
    """error display for deactivating an inactive ruleset"""
    if name == None:
        return("%sruleset is already inactive" %(name))
    else:
        return("%sruleset %s is already inactive" %(Fore.RED, name))


def end_ended_scene_error(name):
    """error display for trying to end an ended scene"""
    return("%s%s is already ended." %(Fore.RED, name))


def library_not_found_error(name):
    """error display for nonexistent library"""
    return("%sLibrary %s does not exist or is not loaded." %(Fore.RED, name)) 


def not_directory_error(name):
    """error display for using al to add a single file"""
    return("%s%s is not a directory. Are you trying to add a notebook?" %(Fore.RED, name)) 


def not_file_error(name):
    """errror  display for using a to add a library"""
    return("%s%s is a directory. Are you trying to add a library?" %(Fore.RED, name)) 


def not_notebook_error(name):
    """error display for trying to add something that isn't a notebook"""
    return("%sThe file %s is not a notebook file." %(Fore.RED, name)) 


def duplicate_notebook_error(name, library_list):
    """ error display for doing operations on a notebook that exists in two places""" 
    from src.praxxis.sqlite import sqlite_library
    print("%sThe notebook %s exists in two places. Specify which library to choose from." %(Fore.RED, name)) 

    i = 0
    for library in library_list:
        i += 1
        print("\t%s.\t%s" %(i, library))


def duplicate_notebook_warning(name):
    """warning display for loading a notebook twice."""
    print("%sThe notebook %s has already been loaded. Reimporting." %(Fore.YELLOW, name))


def duplicate_sync_warning(duplicates):
    """warning for syncing libraries with notebooks that have already been loaded"""
    if len(duplicates) == 1:
        print("%sThe notebook %s was already loaded. Reimporting." %(Fore.YELLOW, duplicates[0]))
    else:
        print("%sThe notebooks") %(Fore.YELLOW)
        for duplicate in duplicates:
            print("%s\t%s") %(Fore.YELLOW, duplicate)
        print("%swere already loaded. Reimporting. " %(Fore.YELLOW)) 


def version_error():
    """error for using the wrong python version"""
    import sys
    return("praxxis requires python 3.6. Your version is %s.%s which is incompatable. Please update python."  %(sys.version_info.major, sys.version_info.minor))


def last_active_scene_error(name):
    """error display for trying to end the last active scene"""
    return("%s%s is your last active scene. Make a new scene, or resume an old one." %(Fore.RED, name)) 


def scene_ended_error(name):
    """error display for trying to switch to an ended scene"""
    return("%scan't switch to %s, because the scene has ended. Resume the scene or make a new one." %(Fore.RED, name)) 

 
def editor_not_found_error(editor):
    """ the error display for not having a text editor"""
    return("%sCould not find editor %s" %(Fore.RED, editor)) 


def ads_not_found_error(ads_path):
    """ the error display for not being able to find an ADS installation"""
    return("%sCould not find installation of ADS at %s" %(Fore.RED, ads_path)) 


def papermill_error(error):
    """error display for papermill errors"""
    print("%sPAPERMILL ERROR" %(Fore.RED))
    print(error)


def no_tagged_cell_warning():
    """warning display for having no tagged cell"""
    print("%sWarning: no tagged cell located. No parameters will be injected for this notebook." %(Fore.YELLOW))


def settings_invalid_ordinal(user_input):
    """error display for bad ordinal input"""
    print("%sBad input: %s is not an ordinal in the list. Please try again."  %(Fore.RED, user_input))


def telem_off_warning():
    """warning display for telemetry being of"""
    print("%sWarning: telemetry is disabled. Turn it on in the settings utility (prax u)" %(Fore.YELLOW))


def telem_not_init_warning():
    """warning display for uninitialized telemetry"""
    print("%s Warning: telemetry is not set up. Use the settings utility (prax u) to enable it." %(Fore.YELLOW)) 


def display_telem_unsent(backlog):
    """warning display for unsent telemetry"""
    print("%sWarning: The last %s output files have not sent. Consider checking server settings with \"prax u\"."  %(Fore.YELLOW, backlog))
    print("%sAttempting to send %s output files now." %(Fore.YELLOW, backlog+1)) 
    

def display_ruleset_num_input_warning(num):
    """warning display for a number being interpreted as a string in a ruleset"""
    print("%sWarning: The number %s is not in the notebook list range and will be interpreted as the string \"%s\"" %(Fore.YELLOW, num, num))


def predictions_ordinal_not_in_list_error():
    """error message for invalid input when making a rule"""
    print("%sThe input was invalid. Please re-enter your list of notebook predictions." %(Fore.RED)) 


def invalid_ruleset_import(name):
    """error fir importing an invalid ruleset""" 
    if name == None:
        return("%sThis does not appear to be the path to a valid .db file" %(Fore.RED) )
    else:
        return("%s%s is not the path to a valid .db file"  %(Fore.RED, name)) 


def repo_exists_warning():
    """warning that a repo has already been imported"""
    print("%sThat repo already exists. Cloning and reimporting." %(Fore.YELLOW)) 


def invalid_rule_definition(name):
    """error for trying to import an invalid rule"""
    print("%sThe rule definition for rule %s is invalid. This rule will not be imported." %(Fore.RED, name)) 


def empty_history_error():
    """error for empty history on an operation that requires history"""
    return("%sThis operation cannot be run on an empty history." %(Fore.RED))


def tensorflow_version_error():
    """error for running an old version of tensorflow"""
    import sys
    print("%spraxxis's model is built with tensorflow, which requires python <=3.6. Your version is %s.%s , which is incompatible." %(Fore.RED, sys.version_info.major, sys.version_info.minor) +
                " Consider changing your python version or running in a virtual environment to get model-based predictions for next actions.")


def pytest_windows_permissions_error(error):
    """error for pytest hitting a windows permissions error)"""
    if "Windows permissions failure" in error:
        return error
    else:
        return "%sWindows permissions failure -- try re-running to resolve (Error %s)" %(Fore.RED, error)
