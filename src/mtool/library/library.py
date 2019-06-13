import os

def init_library(root, library_db):
    from src.mtool.util import sqlite_util
    
    if not os.path.exists(root):
        os.mkdir(root)
        
    if not os.path.exists(library_db):
        sqlite_util.init_library_db(library_db)

def load_libraries(root, library_db):
    directories = [ name for name in os.listdir(root) if os.path.isdir(os.path.join(root, name)) ]
    
    for directory in directories:
        load_library(os.path.join(root, directory), library_db)

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
    for root, dirs, files in os.walk(root, topdown=False):
        for name in files:
            file_name, file_extension = os.path.splitext(name)
            if(file_extension == ".ipynb"):
                file_root = os.path.join(root, name)
                sqlite_util.load_notebook(library_db, file_root, file_name, library_name)