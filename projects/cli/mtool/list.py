"""
This file prints a list of all notebooks on the machine.

Dependencies within mtool: mtool/mtool.py
"""
import sys
import os

# Include the mtool subfolder folder
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), "mtool"))

import mtool

m = mtool.MTool(sys.argv)

counter = 0
items = []

display_format_string = "\t{0}.\t{1} ({2})"

def display(filename):
    """Displays a notebook name as part of a list.
    
    Keyword arguments:
    filename -- notebook name to display
    """
    global counter
    global items
    global display_format_string
    counter += 1

    notebook = m.notebook(filename)

    m.log.info(display_format_string.format(str(counter), notebook.name, notebook.library_name))
    items.append([counter, notebook.name, notebook.library_name])

m.log.section("List notebooks")

if (m.list_exist):
    for item in m.get_list:
        m.log.info(display_format_string.format(str(item[0]), item[1], item[2]))
else:
    m.for_each_notebook(display)
    m.write_list(items)