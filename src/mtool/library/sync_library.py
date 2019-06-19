"""
    This file loads libraries into the library database file
"""

import os

def sync_libraries(library_root, library_db):
    """ loads libraries from the library root you supply, into the library db"""
    from src.mtool.cli import display
    from src.mtool.util import sqlite_util

    directories = [ name for name in os.listdir(library_root) if os.path.isdir(os.path.join(library_root, name)) ]
    sqlite_util.clear_loaded_libararies(library_db)   
    
    first = True
    for directory in directories:
        this_library_root = os.path.join(library_root, directory)
        sync_library(this_library_root, library_db)
        display.display_loaded_library(this_library_root, first)
        #first = False


def sync_library(library_root, library_db):
    """ loads the individual library specified by the library root passed in, into the library db""" 
    from src.mtool.util import sqlite_util
    readme_location = os.path.join(library_root, "README.md")
    readme_data = "No Readme"
    dirname = library_root.split(os.path.sep)[-1]
    if os.path.isfile(readme_location):
         f = open(readme_location, "r")
         readme_data = "  ".join(f.readlines()[:3])

    sqlite_util.load_library(library_db, library_root, readme_data, dirname)
    sync_notebooks(library_root, library_db, dirname)


def sync_notebooks(library_root, library_db, library_name):
    """ loads the individual notebooks in the library root into the library db""" 
    from src.mtool.util import sqlite_util
    from src.mtool.cli import display
    from src.mtool.notebook import notebook
    first = True
    for library_root, dirs, files in os.walk(library_root, topdown=False):
        for name in files:
            file_name, file_extension = os.path.splitext(name)
            if(file_extension == ".ipynb"):
                file_root = os.path.join(library_root, name)

                notebook_data = notebook.Notebook([file_root, file_name, library_name])
                for environment in notebook_data._environmentVars:
                    sqlite_util.set_notebook_environments(library_db, file_name, environment[0], environment[1])
                sqlite_util.load_notebook(library_db, file_root, file_name, library_name)
                display.display_loaded_notebook(name, first)
                first = False
