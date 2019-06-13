import os

def init_library(root, library_db):
    from src.mtool.util import sqlite_util
    from src.mtool.cli import display

    if not os.path.exists(root):
        os.mkdir(root)
        display.display_init_libraries_folder(root)

    if not os.path.exists(library_db):
        sqlite_util.init_library_db(library_db)
        display.display_init_libraries_db(library_db)
