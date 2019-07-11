"""
Searches notebooks for search term using a sql query, and calls the display function
"""
import os

def search_notebook(args, library_db, current_scene_db, start, end):
    """ searches and displays loaded notebooks"""
    from src.mtool.util.sqlite import sqlite_notebook
    from src.mtool.display import display_notebook
    search_term = args.term
    notebook_list = display_notebook.display_search(search_term, sqlite_notebook.search_notebooks(library_db, search_term, start, end))
    sqlite_notebook.write_list(current_scene_db, notebook_list)
    return notebook_list