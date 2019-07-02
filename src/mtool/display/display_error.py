"""
This file contains all of the error messages
"""

from colorama import init, Fore, Style
init()

def env_not_found_error(name):
    """the error display for environments not being found"""
    print(f"{Fore.RED}environment {name} not found")


def notebook_load_error(name):
    print(f"\t{Fore.RED}there is something wrong with {name}. mtool will still load it, but it might not run.{Style.RESET_ALL}")


def scene_does_not_exist_error(name):
    """the error display for scenes not existing"""
    print(f"{Fore.RED}scene {name} does not exist")


def notebook_does_not_exist_error(name):
    """the error display for notebooks not existing"""
    print(f"{Fore.RED}scene {name} does not exist")


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
