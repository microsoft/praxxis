"""
This file prints a list of all notebooks on the machine.

Dependencies within mtool: mtool/mtool.py
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
        notebook.Notebook.for_each_notebook(display)
        m.write_list(items)


def display(notebook):
    """Displays a notebook name as part of a list.
    
    Keyword arguments:
    filename -- notebook name to display
    """
    global counter
    global items
    global display_format_string
    counter += 1

    l.info(display_format_string.format(str(counter), notebook.name, notebook.library_name))
    items.append([counter, notebook.name, notebook.library_name])

