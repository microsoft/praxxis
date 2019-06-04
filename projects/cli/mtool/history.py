"""
This file prints the history in the current scene.

Dependencies within mtool: mtool/mtool.py
"""
import os
import sys

# Include the mtool subfolder folder
#
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), "mtool"))

import mtool

m = mtool.MTool(sys.argv)
m.log.header("History for scene", m.current_scene)

uniquify = False
items = []
counter = 0

def display(notebook_name, library_name):
    """Print a notebook when printing history"""
    global counter
    global items

    counter += 1
    m.log.indent("{0}. {1} ({2})".format(str(counter), notebook_name, library_name))
    items.append([counter, notebook_name, library_name])

m.for_each_notebook_in_scene_history(uniquify, display)
m.write_list(items)

