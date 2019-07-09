"""
This file contains all of the error messages
"""

from colorama import init, Fore, Style
init(autoreset=True)

def env_not_found_error(name):
    """the error display for environments not being found"""
    return(f"{Fore.RED}environment {name} not found")


def notebook_load_error(name):
    print(f"\t{Fore.RED}there is something wrong with {name}. mtool will still load it, but it might not run.{Style.RESET_ALL}")


def scene_not_found_error(name):
    """the error display for scenes not existing"""
    if name == None:
        return(f"{Fore.RED}scene does not exist")
    else:
        return(f"{Fore.RED}scene {name} does not exist")


def notebook_not_found_error(name):
    """the error display for notebooks not existing"""
    if name == None:
        return(f"{Fore.RED}notebook does not exist")
    else:
        return(f"{Fore.RED}notebook {name} does not exist")


def end_ended_scene_error(name):
    return(f"{Fore.RED}{name} is already ended.")


def last_active_scene_error(name):
    """the error display for trying to end the last active scene"""
    print(f"{Fore.RED}{name} is your last active scene. Make a new scene, or resume an old one.")


def scene_ended_error(name):
    """the error display for trying to switch to an ended scene"""
    print(f"{Fore.RED}can't switch to {name}, because the scene has ended. Resume the scene or make a new one.")
    

def papermill_error(error):
        """the error display for papermill errors"""
        print(f"{Fore.RED}PAPERMILL ERROR")
        print(error)

def no_tagged_cell_warning():
    """the warning display for having no tagged cell"""
    print(f"{Fore.YELLOW}Warning: no tagged cell located. No parameters will be injected for this notebook.")

def settings_invalid_ordinal(userIn):
    """the error display for bad ordinal input"""
    print(f"{Fore.RED}Bad input: {userIn} is not an ordinal in the list. Please try again.")

def telem_off_warning():
    """the warning display for telemetry being off"""
    print(f"{Fore.YELLOW}Warning: telemetry is disabled. Turn it on in the settings utility (m u)")

def telem_not_init_warning():
    """the warning display for uninitialized telemetry"""
    print(f"{Fore.YELLOW}Warning: telemetry is not set up. Use the settings utility (m u) to enable it.")

def display_telem_unsent(backlog):
    """the warning display for unsent telemetry"""
    print(f"{Fore.YELLOW}Warning: The last {backlog} output files have not sent. Consider checking server settings with \"m u\".")
    print(f"{Fore.YELLOW}Attempting to send {backlog+1} output files now.")
    
