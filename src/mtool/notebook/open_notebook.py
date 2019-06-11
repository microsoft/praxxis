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
from src.mtool.notebook import notebook

m = None

def open_notebook(arvs):
    """Open a notebook"""
    global m
    m = mtool.Mtool(arvs)
    m.set_environment_overrides_for_scene()



def load_notebook(filename):
    """Opens a notebook in Azure Data Studio

    Keyword arguments:
    filename -- name of notebook to open
    """
    #nb = notebook.Notebook(filename)
    outputfile = filename
    #outputfile = nb.get_local_copy_filename('.ipynb')
    shutil.copyfile(filename, outputfile)
    subprocess.Popen([m.azure_data_studio_binary_location, outputfile])
