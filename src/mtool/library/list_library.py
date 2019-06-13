"""
This file prints a list of all notebook libraries installed on this machine.

Dependencies within mtool: mtool/mtool.py
"""
import os
import sys
import json

def list_library(library_root, library_db):
        from src.mtool.library import library
        from src.mtool.util import sqlite_util
        library.init_library(library_root, library_db)
        library.load_libraries(library_root, library_db)
        libraries = ", ".join(list(sum(sqlite_util.list_libraries(library_db, 0, 10), ())))
        print(f"libraries: {libraries}")


def display(root, library_name):
    """Print the library's name and description (from a readme).

    Keyword arguments:
    root -- file path to the dir where the library folder is
    library_name -- name of the library folder
    """
    library_readme_filename = os.path.join(os.path.expandvars(root), library_name, "README.md")

    description = ""
    if os.path.isfile(library_readme_filename):
        with open(library_readme_filename, 'r') as file:
            description = file.read()




