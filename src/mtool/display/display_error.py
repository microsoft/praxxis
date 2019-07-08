"""
This file contains all of the error messages
"""

from colorama import init, Fore, Style
init(autoreset=True)

def env_not_found_error(name):
    """the error display for environments not being found"""
    print(f"{Fore.RED}environment {name} not found")


def notebook_load_error(name):
    print(f"\t{Fore.RED}there is something wrong with {name}. mtool will still load it, but it might not run.{Style.RESET_ALL}")


def scene_does_not_exist_error(name):
    """the error display for scenes not existing"""
    if name == None:
        print(f"{Fore.RED}scene does not exist")
    else:
        print(f"{Fore.RED}scene {name} does not exist")


def notebook_does_not_exist_error(name):
    """the error display for notebooks not existing"""
    if name == None:
        print(f"{Fore.RED}notebook does not exist")
    else:
        print(f"{Fore.RED}notebook {name} does not exist")


def last_active_scene_error(name):
    """the error display for trying to end the last active scene"""
    print(f"{Fore.RED}{name} is your last active scene. Make a new scene, or resume an old one.")


def scene_ended_error(name):
    """the error display for trying to switch to an ended scene"""
    print(f"{Fore.RED}can't switch to {name}, because the scene has ended. Resume the scene or make a new one")


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

def display_telem_off():
    """the warning display for telemetry being off"""
    print(f"{Fore.YELLOW}Warning: telemetry is disabled. Turn it on in the settings utility (m u)")

def display_telem_not_init():
    """the warning display for uninitialized telemetry"""
    print(f"{Fore.YELLOW}Warning: telemetry is not set up. Use the settings utility (m u) to enable it.")

def display_telem_unsent(backlog):
    """the warning display for unsent telemetry"""
    print(f"{Fore.YELLOW}Warning: The last {backlog} output files have not sent. Consider checking server settings with \"m u\".")
    print(f"{Fore.YELLOW}Attempting to send {backlog+1} output files now.")
    
