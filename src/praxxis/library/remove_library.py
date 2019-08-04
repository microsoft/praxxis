"""
This file removes a library by ordinal or name
"""

def remove_library(args, library_db, query_start, query_end):
    """removes a library by ordinal or name"""
    from src.praxxis.sqlite import sqlite_library
    from src.praxxis.display import display_library
    import os

    name = args.name

    if name.isdigit():
        from src.praxxis.library import library
        name = library.get_library_by_ordinal(library_db, name, query_start, query_end)
    
    sqlite_library.check_library_exists(library_db, name)
    sqlite_library.remove_library(library_db, name)
    display_library.display_remove_success(name)

