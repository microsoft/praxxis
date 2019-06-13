"""
This file prints a list of all notebooks on the machine.

Dependencies within mtool: mtool.py, log.py, notebook.py
Goal dependencies: notebook.py
"""

import os
        
def list_notebook(scene_root, library_db, history_db, current_scene_db, start, stop):
    from src.mtool.util import sqlite_util
    from src.mtool.cli import display
    notebooks = sqlite_util.list_notebooks(library_db, start, stop)
    sqlite_util.write_list(current_scene_db, notebooks)
    display.display_list_notebook(notebooks)