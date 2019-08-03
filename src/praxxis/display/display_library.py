"""
This file contains all of the display functions for libraries
"""

def display_init_libraries_folder(root):
    """the display function for creating new libraries folder"""
    print("Created libraries directory at %s" %(root)) 


def display_init_libraries_db(db_root):
    """the display function for initializing the libraries db"""
    print("Created libraries database at %s" %(db_root)) 


def display_loaded_library(root, first):
    """the display function for loading libarires"""
    if first:
        print("Loaded library at:\n\t%s" %(root)) 
    else:
        print("\t%s" %(root)) 


def loaded_notebook_message():
    """the display function for loading a notebook"""
    print("Loaded notebook:")


def display_init_git_library(root):
    """ the display function for cloning a git repo"""
    print("Created git library at %s" %(root)) 


def display_loaded_notebook(name):
    """ the display function for loading a notebook"""
    print("\t%s" %(name)) 


def display_libraries(libraries):
    """the display function for listing libraries"""
    print("Libraries:")
    i = 0
    for library in libraries:
        i+=1
        print("\t%s.\t%s" %(i, library[0])) 


def display_remove_success(name):
    """ the display function for removing a library"""
    print("%s was successfully removed. " %(name)) 
    
