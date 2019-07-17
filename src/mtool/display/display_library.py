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
    print("Loaded notebook:")


def display_loaded_notebook(name):
    print(f"\t{name}")


def display_libraries(libraries):
    """the display function for listing libraries""" 
    libraries = "\n\t".join(list(sum(libraries, ())))
    print(f"Loaded libraries:\n\t{libraries}")


def display_remove_success(name):
    print(f'{name} was successfully removed. ')