"""
This file prints a list of all notebooks on the machine.

Dependencies within mtool: mtool.py, log.py, notebook.py
Goal dependencies: notebook.py
"""

import os
        
def list_notebook(root):
    from src.mtool.util import sqlite_util
    sqlite_util.list_notebooks(root, 0, 10)
    notebooks = ", ".join(list(sum(sqlite_util.list_notebooks(root, 0, 10), ())))
    print(f"Notebooks: {notebooks}")
