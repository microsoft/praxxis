"""
Searches notebooks for search term using a sql query, and calls the display function
"""
import os

def search_notebook(args, library_db, current_scene_db, start, end):
    """ searches and displays loaded notebooks"""
    from src.praxxis.sqlite import sqlite_notebook
    from src.praxxis.display import display_notebook

    search_term = args.term
    notebooks = sqlite_notebook.search_notebooks(library_db, search_term, start, end)
    display_notebook.display_search(search_term, notebooks)
    sqlite_notebook.write_list(current_scene_db, notebooks)
    return notebooks