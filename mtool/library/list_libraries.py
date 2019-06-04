import os
import sys
import json

from mtool.cli import mtool

m = None

def list_libraries(args):
    global m
    m = mtool.MTool(args)
    m.log.header("Notebook libraries installed on this machine")
    m.for_each_library(display)


def display(root, library_name):
    library_readme_filename = os.path.join(os.path.expandvars(root), library_name, "README.md")

    description = ""
    if os.path.isfile(library_readme_filename):
        with open(library_readme_filename, 'r') as file:
            description = file.read()

    m.log.indent("{0} ({1})".format(library_name, description.replace("# ", "", 1)))


