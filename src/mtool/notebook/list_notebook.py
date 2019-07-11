"""
This file lists all of the notebooks loaded into the library db file
"""
        
def list_notebook(library_db, current_scene_db, start, stop):
    """ gets the notebooks from the sqlite db and displays them through its display function"""
    from src.mtool.util.sqlite import sqlite_notebook
    from src.mtool.display import display_notebook

    notebooks = sqlite_notebook.list_notebooks(library_db, start, stop)
    sqlite_notebook.write_list(current_scene_db, notebooks)
    display_notebook.display_list_notebook(notebooks)
    return notebooks
