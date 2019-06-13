"""
This file prints a list of all notebooks on the machine.

Dependencies within mtool: mtool.py, log.py, notebook.py
Goal dependencies: notebook.py
"""

import os
        
def list_notebook(root):
    from src.mtool.util import sqlite_util
    from src.mtool.cli import display
    notebooks = sqlite_util.list_notebooks(root, 0, 10)
    display.display_list_notebook(notebooks)