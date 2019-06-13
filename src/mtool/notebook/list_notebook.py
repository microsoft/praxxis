"""
This file prints a list of all notebooks on the machine.

Dependencies within mtool: mtool.py, log.py, notebook.py
Goal dependencies: notebook.py
"""

import os
        
def list_notebook(scene_root, library_db, history_db):
    from src.mtool.util import sqlite_util
    from src.mtool.cli import display
    notebooks = sqlite_util.list_notebooks(library_db, 0, 10)
    scene = sqlite_util.get_current_scene(history_db)
    sqlite_util.write_list(os.path.join(scene_root, scene, f"{scene}.db"), notebooks)
    display.display_list_notebook(notebooks)