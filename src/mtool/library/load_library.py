import os

def load_libraries(root, library_db):
    from src.mtool.cli import display
    directories = [ name for name in os.listdir(root) if os.path.isdir(os.path.join(root, name)) ]
   
    first = True
    for directory in directories:
        library_root = os.path.join(root, directory)
        load_library(library_root, library_db)
        display.display_loaded_library(library_root, first)
        first = False


def load_library(root, library_db):
    from src.mtool.util import sqlite_util
    readme_location = os.path.join(root, "README.md")
    readme_data = "No Readme"
    dirname = root.split(os.path.sep)[-1]
    if os.path.isfile(readme_location):
         f = open(readme_location, "r")
         readme_data = "  ".join(f.readlines()[:3])

    sqlite_util.load_library(library_db, root, readme_data, dirname)
    load_notebooks(root, library_db, dirname)


def load_notebooks(root, library_db, library_name):
    from src.mtool.util import sqlite_util
    from src.mtool.cli import display

    first = True
    for root, dirs, files in os.walk(root, topdown=False):
        for name in files:
            file_name, file_extension = os.path.splitext(name)
            if(file_extension == ".ipynb"):
                file_root = os.path.join(root, name)
                sqlite_util.load_notebook(library_db, file_root, file_name, library_name)
                display.display_loaded_notebook(name, first)
                first = False
