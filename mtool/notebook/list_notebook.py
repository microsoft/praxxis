"""
This file prints a list of all notebooks on the machine.

Dependencies within mtool: mtool/mtool.py
"""

import sys
import os

from mtool.cli import mtool

m = None
counter = 0
items = []
display_format_string = "\t{0}.\t{1} ({2})"

def list_notebook(args):
    """Display each notebook found on machine"""
    global m
    m = mtool.MTool(args)
    m.log.section("List notebooks")

    if (m.list_exist and m.get_list != []):
        for item in m.get_list:
            m.log.info(display_format_string.format(str(item[0]), item[1], item[2]))
    else:
        curr = os.getcwd()
        root = os.path.join(curr, "..\\library")
        m.for_each_notebook(root, display)
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

    m.log.info(display_format_string.format(str(counter), notebook.name, notebook.library_name))
    items.append([counter, notebook.name, notebook.library_name])

