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

    first = True
    for directory in directories:
        this_library_root = os.path.join(library_root, directory)
        sync_library(this_library_root, library_db)
        display_library.display_loaded_library(this_library_root, first)
        #first = False
    return 0


def sync_library(library_root, library_db, library_name=None, remote=None):
    """ loads the individual library specified by the library root passed in, into the library db""" 
    from src.mtool.util.sqlite import sqlite_library
    from src.mtool.util import error

    readme_location = os.path.join(library_root, "README.md")
    readme_data = "No Readme"

    if library_name == None:
        library_name = library_root.split(os.path.sep)[-1]

    counter = 0
    while sqlite_library.library_exists(library_db, library_name):
        library_name = f"{library_name}-{counter + 1}"

    if os.path.isfile(readme_location):
         f = open(readme_location, "r")
         readme_data = "  ".join(f.readlines()[:3])

    sqlite_library.sync_library(library_db, library_root, readme_data, library_name, remote)
    sync_notebooks(library_root, library_db, library_name)


def sync_notebooks(library_root, library_db, library_name):
    """ loads the individual notebooks in the library root into the library db""" 
    from src.mtool.util.sqlite import sqlite_library
    from src.mtool.util.sqlite import sqlite_environment
    from src.mtool.util.sqlite import sqlite_notebook
    from src.mtool.util import error

    from src.mtool.display import display_library
    from src.mtool.display import display_error
    from src.mtool.notebook import notebook
    first = True
    duplicates = []
    for library_root, dirs, files in os.walk(library_root, topdown=False):
        for name in files:
            # for every notebook in the files found by the os.walk
            file_name, file_extension = os.path.splitext(name)
            if(file_extension == ".ipynb"):
                # if the file is a notebook file
                file_root = os.path.join(library_root, name)
                #set the file root for the db 
                if first:
                    display_library.loaded_notebook_message()
                    #if it's the first notebook, display notebook loaded message
                try:
                    notebook_data = notebook.Notebook([file_root, file_name, library_name])
                    #create a notebook object out of the file data
                    for environment in notebook_data._environmentVars:
                        #load the environment variables out of the notebook object and into the db
                        sqlite_environment.set_notebook_environments(library_db, file_name, environment[0].strip(), environment[1])
                    display_library.display_loaded_notebook(name)
                    #display that the library has been successfully loaded
                except:
                    display_error.notebook_load_error(name)
                    #if there was a problem loading the notebook, show an error.

                try:
                    sqlite_notebook.check_notebook_exists(library_db, file_name)
                except error.NotebookNotFoundError:
                    pass
                else:
                    duplicates.append(name)

                sqlite_library.load_notebook(library_db, file_root, file_name, library_name)
                #finally, load the notebook's data into the db
                first = False
    if not duplicates == []:
        display_error.duplicate_sync_warning(duplicates)