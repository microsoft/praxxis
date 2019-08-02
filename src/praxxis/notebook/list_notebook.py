"""
This file lists all of the notebooks loaded into the library db file
"""
        
def list_notebook(library_db, current_scene_db, query_start, query_end):
    """ gets the notebooks from the sqlite db and displays them through its display function"""
    from src.praxxis.sqlite import sqlite_notebook
    from src.praxxis.display import display_notebook

    notebooks = sqlite_notebook.list_notebooks(library_db, query_start, query_end)
    sqlite_notebook.write_list(current_scene_db, notebooks)
    display_notebook.display_list_notebook(notebooks)
    return notebooks
