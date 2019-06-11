"""
This file prints a list of all notebooks on the machine.

Dependencies within mtool: mtool.py, log.py, notebook.py
Goal dependencies: notebook.py
"""

import sys
import os

from src.mtool.cli import mtool 
from src.mtool.util import log
from src.mtool.notebook import notebook

l = None
m = None
counter = 0
items = []
display_format_string = "\t{0}.\t{1} ({2})"

def display(nb):
    """Displays a notebook name as part of a list.
    
    Keyword arguments:
    filename -- notebook name to display
    """
    global counter
    global items
    global display_format_string
    counter += 1

    l.info(display_format_string.format(str(counter), nb.name, nb.library_name))
    items.append([counter, nb.name, nb.library_name])

def display_each_notebook(root = "", notebooks = []):
    """Calls fn on every notebook in directory

    Default: calls fn on every notebook in library folder
    """
    # TODO: %APPDATA% is windows specific and gross
    # note: the weird default variable thing is because you can't call
    #   a function in a arguments list :/
    if root == "":
        root = os.path.join(os.getenv('APPDATA'),"mtool","library")
    os.chdir(root)
    currDir = os.listdir()
    subDirs = []
    for item in currDir:
        if os.path.isfile(item) and item.endswith(".ipynb"):
            path = os.getcwd()
            nb = notebook.Notebook(os.path.join(path, item))
            notebooks.append(item)
            display(nb)
        elif os.path.isdir(item):
            subDirs.append(item)
    while subDirs != []:
        thisSubDir = subDirs.pop()
        subDirPath = os.path.join(root, thisSubDir)
        display_each_notebook(subDirPath, notebooks)
        
def list_notebook(args):
    """Display each notebook found on machine"""
    global l
    global m
    l = log.Log()
    m = mtool.Mtool(args)
    l.section("List notebooks")

    if (m.list_exist and m.get_list != []):
        for item in m.get_list:
            l.info(display_format_string.format(str(item[0]), item[1], item[2]))
    else:
        display_each_notebook()
        m.write_list(items)

