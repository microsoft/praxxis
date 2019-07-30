"""
This file contains all of the display functions for libraries
"""

def display_init_libraries_folder(root):
    """the display function for creating new libraries folder"""
    print(f"Created libraries directory at {root}")


def display_init_libraries_db(db_root):
    """the display function for initializing the libraries db"""
    print(f"Created libraries database at {db_root}")


def display_loaded_library(root, first):
    """the display function for loading libarires"""
    if first:
        print(f"Loaded library at:\n\t{root}")
    else:
        print(f"\t{root}")


def loaded_notebook_message():
    """the display function for loading a notebook"""
    print("Loaded notebook:")


def display_init_git_library(root):
    """ the display function for cloning a git repo"""
    print(f"Created git library at {root}")


def display_loaded_notebook(name):
    """ the display function for loading a notebook"""
    print(f"\t{name}")


def display_libraries(libraries):
    """the display function for listing libraries"""
    print(f"Libraries:")
    i = 0
    for library in libraries:
        i+=1
        print(f"\t{i}.\t{library[0]}")


def display_remove_success(name):
    """ the display function for removing a library"""
    print(f'{name} was successfully removed. ')
    
