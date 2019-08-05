"""
This file removes a notebook.
"""

def remove_notebook(args, library_db, current_scene_db):
    """remove a notebook from sqlite database"""
    from src.praxxis.sqlite import sqlite_library
    from src.praxxis.sqlite import sqlite_notebook
    from src.praxxis.notebook import notebook
    from src.praxxis.notebook import list_notebook
    from src.praxxis.display import display_notebook

    name = args.name

    notebook_data = notebook.get_notebook(current_scene_db, library_db, name)
    sqlite_library.remove_notebook(library_db, notebook_data[1], notebook_data[2])
    display_notebook.display_remove_success(name)
