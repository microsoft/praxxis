"""
Searches notebooks for search term using a sql query, and calls the display function
"""

def search_notebook(args, library_db, start, end):
    """ searches and displays loaded notebooks"""
    from src.mtool.util import sqlite_util
    from src.mtool.cli import display
    search_term = args.term
    display.display_search(search_term, sqlite_util.search_notebooks(library_db, search_term, start, end))
