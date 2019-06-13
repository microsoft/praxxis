"""
This file prints a list of all notebooks on the machine.

Dependencies within mtool: mtool.py, log.py, notebook.py
Goal dependencies: notebook.py
"""

import sys
import os
 
from src.mtool.util import log
from src.mtool.notebook import notebook
from src.mtool.util import sqlite_util

l = None
counter = 0
display_format_string = "\t{0}.\t{1} ({2})"

def display(nb):
    """Displays a notebook name as part of a list.
    
    Keyword arguments:
    filename -- notebook name to display
    """
    global counter
    global display_format_string


    l.info(display_format_string.format(str(counter), nb.name, nb.library_name))

def display_each_notebook(root):
    """Calls fn on every notebook in directory"""
    global counter
    notebooks = []
    os.chdir(root)
    currDir = os.listdir()
    subDirs = []
    for item in currDir:
        if os.path.isfile(item) and item.endswith(".ipynb"):
            path = os.getcwd()
            nb = notebook.Notebook(os.path.join(path, item))
            counter += 1
            notebooks.append((counter, item, os.path.join(root, item)))
            display(nb)
        elif os.path.isdir(item):
            subDirs.append(item)
    while subDirs != []:
        thisSubDir = subDirs.pop()
        subDirPath = os.path.join(root, thisSubDir)
        notebooks += display_each_notebook(subDirPath)
    return notebooks
        
def list_notebook(args, root):
    """Display each notebook found on machine"""
    global l
    l = log.Log()
    l.section("List notebooks")

    library_root = os.path.join(root, "library")
    notebooks = display_each_notebook(library_root)

    scene_root = os.path.join(root, "scene")
    history_db = os.path.join(scene_root, "current_scene.db")
    db_file = os.path.join(scene_root, sqlite_util.get_current_scene(history_db), sqlite_util.get_current_scene(history_db) + ".db")
    sqlite_util.write_scene_list(db_file, notebooks)
    

