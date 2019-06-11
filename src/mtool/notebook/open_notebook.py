"""
This file opens a notebook in Azure Data Studio.

Dependencies within mtool: notebook.py, scene.py
"""

import os
import sys
import shutil
import subprocess

import pypandoc

from src.mtool.notebook.notebook import Notebook
from src.mtool.scene.scene import Scene

def open_notebook(args):
    """Open a notebook"""
    # notebook = the number of the notebook
    notebook_filename = Scene.ordinal_to_list_item(args.notebook)
    load_notebook(notebook_filename)
    #load_notebook(m.args.ordinal_to_list_item(args)[0])

def azure_data_studio_binary_location():
    ##TODO: THIS IS WINDOWS SPECIFIC
    """Returns location of ADS binary"""
    return os.path.join(os.getenv('LOCALAPPDATA'), 'Programs', 'Azure Data Studio', 'azuredatastudio')


def convert_to_html(filename, html_outputfile):
    pypandoc.convert_file(filename, 'html', outputfile=html_outputfile)

def display_to_console(filename):
    print(pypandoc.convert_file(filename, 'asciidoc'))

def load_notebook(filename):
    """Opens a notebook in Azure Data Studio

    Keyword arguments:
    filename -- name of notebook to open
    """
    #nb = notebook.Notebook(filename)
    #outputfile = nb.get_local_copy_filename('.ipynb')
    #shutil.copyfile(filename, outputfile)
    subprocess.Popen([azure_data_studio_binary_location(), filename])
