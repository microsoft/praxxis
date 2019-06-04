"""
This file prints a list of all notebook libraries installed on this machine.

Dependencies within mtool: mtool/mtool.py
"""
import os
import sys
import json

from mtool.cli import mtool

m = None

def list_library(args):
    global m
    m = mtool.MTool(args)
    m.log.header("Notebook libraries installed on this machine")
    m.for_each_library(display)


def display(root, library_name):
    """Print the library's name and description (from a readme).

    Keyword arguments:
    root -- file path to the dir where the library folder is
    library_name -- name of the library folder
    """
    library_readme_filename = os.path.join(os.path.expandvars(root), library_name, "README.md")

    description = ""
    if os.path.isfile(library_readme_filename):
        with open(library_readme_filename, 'r') as file:
            description = file.read()

    m.log.indent("{0} ({1})".format(library_name, description.replace("# ", "", 1)))


