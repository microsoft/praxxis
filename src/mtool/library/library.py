"""
This file initializes the library directory and db for all library calls
"""

def init_library(library_root, library_db):
    """checks if the library library_root exists, and creates it,
    then checks if the library database exists, and creates that as well."""
    import os

    from src.mtool.util import sqlite_util
    from src.mtool.cli import display

    if not os.path.exists(library_root):
        os.mkdir(library_root)
        display.display_init_libraries_folder(library_root)

    if not os.path.exists(library_db):
        sqlite_util.init_library_db(library_db)
        display.display_init_libraries_db(library_db)
