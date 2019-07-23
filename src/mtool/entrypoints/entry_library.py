"""
this handles the library section of the CLI.
"""

from src.mtool.util.roots import _library_root
from src.mtool.util.roots import _library_db
from src.mtool.util.roots import _git_root
from src.mtool.util.roots import _query_start
from src.mtool.util.roots import _query_end


def init_library(library_root = _library_root, 
                 library_db = _library_db):
    """
    handles the initialization of the library dbs and directories
    """
    import os
    from src.mtool.sqlite import sqlite_init
    from src.mtool.display import display_library
    
    os.mkdir(library_root)
    display_library.display_init_libraries_folder(library_root)
    sqlite_init.init_library_db(library_db)
    display_library.display_init_libraries_db(library_db)


def add_library(arg,
                library_db = _library_db,
                git_root = _git_root):
    """calls the function to add a library"""
    from src.mtool.library import add_library
    try:
        add_library.add_library(arg, library_db, git_root)
    except Exception as e:
        raise e


def remove_library(arg, 
                   library_db = _library_db,
                   query_start = _query_start,
                   query_end = _query_end,):
    """
    handles removing a library
    """
    from src.mtool.library import remove_library

    remove_library.remove_library(arg, library_db, query_start, query_end)


def list_library(arg, 
                 library_db = _library_db):
    """calls the function to list loaded libraries"""
    from src.mtool.library import list_library
    list_library.list_library(library_db)


def sync_library(arg, 
                 library_root = _library_root,
                 library_db = _library_db):
    """calls the function to load libraries"""
    from src.mtool.library import sync_library
    sync_library.sync_libraries(library_root, library_db)
