def init_library(library_root, library_db):
    import os
    from src.mtool.util.sqlite import sqlite_library
    from src.mtool.display import display_library
    
    os.mkdir(library_root)
    display_library.display_init_libraries_folder(library_root)
    sqlite_library.init_library_db(library_db)
    display_library.display_init_libraries_db(library_db)


def add_library(arg):
    """calls the function to add a library"""
    ##TODO: implement this
    return "coming soon"


def list_library(arg, 
                 library_root,
                 library_db):
    """calls the function to list loaded libraries"""
    from src.mtool.library import list_library
    libraries = list_library.list_library(library_root, library_db)
    return libraries


def sync_library(arg, 
                 library_root,
                 library_db):
    """calls the function to load libraries"""
    from src.mtool.library import sync_library
    libraries = sync_library.sync_libraries(library_root, library_db)
    return libraries
