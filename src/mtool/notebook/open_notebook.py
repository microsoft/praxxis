"""
This file opens a notebook in Azure Data Studio.

Dependencies within mtool: mtool/mtool.py
"""

import os
import sys
import shutil
import subprocess

from src.mtool.cli import mtool
from src.mtool.cli import args
from src.mtool.notebook.notebook import Notebook

m = None

def open_notebook(args):
    """Open a notebook"""
    global m
    # notebook = the number of the notebook
    m = mtool.Mtool(args)
    m.set_environment_overrides_for_scene()
    #load_notebook(m.args.ordinal_to_list_item(args)[0])

def load_notebook(filename):
    """Opens a notebook in Azure Data Studio

    Keyword arguments:
    filename -- name of notebook to open
    """
    #nb = notebook.Notebook(filename)
    outputfile = filename
    print("in load_notebook")
    #outputfile = nb.get_local_copy_filename('.ipynb')
    shutil.copyfile(filename, outputfile)
    subprocess.Popen([m.azure_data_studio_binary_location, outputfile])
