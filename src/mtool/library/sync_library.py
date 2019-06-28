"""
    This file loads libraries into the library database file
"""

import os

def sync_libraries(library_root, library_db):
    """ loads libraries from the library root you supply, into the library db"""
    from src.mtool.display import display_library
    from src.mtool.util.sqlite import sqlite_library
    from src.mtool.util.sqlite import sqlite_environment


    directories = [ name for name in os.listdir(library_root) if os.path.isdir(os.path.join(library_root, name)) ]
    sqlite_library.clear_loaded_libararies(library_db)   
    sqlite_environment.clear_notebook_environments(library_db)   
    
    first = True
    for directory in directories:
        this_library_root = os.path.join(library_root, directory)
        sync_library(this_library_root, library_db)
        display_library.display_loaded_library(this_library_root, first)
        #first = False


def sync_library(library_root, library_db):
    """ loads the individual library specified by the library root passed in, into the library db""" 
    from src.mtool.util.sqlite import sqlite_library
    readme_location = os.path.join(library_root, "README.md")
    readme_data = "No Readme"
    dirname = library_root.split(os.path.sep)[-1]
    if os.path.isfile(readme_location):
         f = open(readme_location, "r")
         readme_data = "  ".join(f.readlines()[:3])

    sqlite_library.load_library(library_db, library_root, readme_data, dirname)
    sync_notebooks(library_root, library_db, dirname)


def sync_notebooks(library_root, library_db, library_name):
    """ loads the individual notebooks in the library root into the library db""" 
    from src.mtool.util.sqlite import sqlite_library
    from src.mtool.util.sqlite import sqlite_environment

    from src.mtool.display import display_library
    from src.mtool.display import display_error
    from src.mtool.notebook import notebook
    first = True
    for library_root, dirs, files in os.walk(library_root, topdown=False):
        for name in files:
            file_name, file_extension = os.path.splitext(name)
            if(file_extension == ".ipynb"):
                file_root = os.path.join(library_root, name)
                if first:
                    display_library.loaded_notebook_message()

                try:
                    notebook_data = notebook.Notebook([file_root, file_name, library_name])
                    for environment in notebook_data._environmentVars:
                        sqlite_environment.set_notebook_environments(library_db, file_name, environment[0].strip(), environment[1])
                    display_library.display_loaded_notebook(name)
                except:
                    display_error.notebook_load_error(name)

                sqlite_library.load_notebook(library_db, file_root, file_name, library_name)
                first = False
