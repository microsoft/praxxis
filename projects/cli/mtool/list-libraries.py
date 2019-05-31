"""
This file DOES A THING

Dependencies within mtool: mtool/mtool.py
"""
import os
import sys
import json

# Include the mtool subfolder folder
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), "mtool"))

import mtool

m = mtool.MTool(sys.argv)

m.log.header("Notebook libraries installed on this machine")

def display(root, library_name):
    library_readme_filename = os.path.join(os.path.expandvars(root), library_name, "README.md")

    description = ""
    if os.path.isfile(library_readme_filename):
        with open(library_readme_filename, 'r') as file:
            description = file.read()

    m.log.indent("{0} ({1})".format(library_name, description.replace("# ", "", 1)))

m.for_each_library(display)

