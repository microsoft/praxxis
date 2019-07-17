from src.mtool.util.roots import _library_root
from src.mtool.util.roots import _library_db

def init_library(library_root = _library_root, 
                 library_db = _library_db):
    import os
    from src.mtool.util.sqlite import sqlite_library
    from src.mtool.display import display_library
    
    os.mkdir(library_root)
    display_library.display_init_libraries_folder(library_root)
    sqlite_library.init_library_db(library_db)
    display_library.display_init_libraries_db(library_db)


def add_library(arg,
                library_db = _library_db):
    """calls the function to add a library"""
    from src.mtool.library import add_library
    try:
        add_library.add_library(arg, library_db)
    except Exception as e:
        raise e
    return 0


def remove_library(arg, 
                   library_db = _library_db):
    from src.mtool.library import remove_library

    remove_library.remove_library(arg, library_db)


def list_library(arg, 
                 library_db = _library_db):
    """calls the function to list loaded libraries"""
    from src.mtool.library import list_library
    libraries = list_library.list_library(library_db)
    return libraries


def sync_library(arg, 
                 library_root = _library_root,
                 library_db = _library_db):
    """calls the function to load libraries"""
    from src.mtool.library import sync_library
    libraries = sync_library.sync_libraries(library_root, library_db)
    return libraries
