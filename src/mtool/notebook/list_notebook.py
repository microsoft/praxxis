"""
This file prints a list of all notebooks on the machine.

Dependencies within mtool: mtool/mtool.py
"""

import sys
import os

from src.mtool.cli import mtool

m = None
counter = 0
items = []
display_format_string = "\t{0}.\t{1} ({2})"

def list_notebook(args):
    """Display each notebook found on machine"""
    global m
    m = mtool.MTool(args)
    m.log.section("List notebooks")

    if (m.list_exist):
        for item in m.get_list:
            m.log.info(display_format_string.format(str(item[0]), item[1], item[2]))
    else:
        m.write_list(items)


def display(filename):
    """Displays a notebook name as part of a list.
    
    Keyword arguments:
    filename -- notebook name to display
    """
    global counter
    global items
    global display_format_string
    counter += 1


