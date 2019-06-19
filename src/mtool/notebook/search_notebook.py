"""
Searches notebooks for search term using a sql query, and calls the display function
"""
import os

def search_notebook(args, library_db, start, end):
    """ searches and displays loaded notebooks"""
    from src.mtool.util import sqlite_util
    from src.mtool.cli import display
    if not os.path.exists(library_db):
        from src.mtool.library.library import init_library
        init_library(os.path.dirname(library_db), library_db)
    search_term = args.term
    display.display_search(search_term, sqlite_util.search_notebooks(library_db, search_term, start, end))
