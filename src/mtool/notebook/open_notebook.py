"""
This file opens a notebook in Azure Data Studio.

Dependencies within mtool: notebook.py, scene.py
"""

import os
import shutil
import subprocess

import pypandoc
import webbrowser
#TODO: the version of pandoc that's on wheel is ... ugly and doesn't support ipynb

from src.mtool.notebook.notebook import Notebook

def open_notebook(args, current_scene_db):
    from src.mtool.util import sqlite_util
    """Open a notebook"""
    # notebook = the number of the notebook
    notebook_filename = sqlite_util.ordinal_to_list_item(current_scene_db, args.notebook)[1]
    display_in_editor(notebook_filename)

def azure_data_studio_binary_location():
    ##TODO: THIS IS WINDOWS SPECIFIC
    """Returns location of ADS binary"""
    return os.path.join(os.getenv('LOCALAPPDATA'), 'Programs', 'Azure Data Studio', 'azuredatastudio')

def display_as_html(filename, html_outputfile):
    pypandoc.convert_file(filename, 'html', outputfile=html_outputfile)
    webbrowser.open(html_outputfile)


def display_in_editor(filename):
    """Opens a notebook in Azure Data Studio

    Keyword arguments:
    filename -- name of notebook to open
    """
    subprocess.Popen([azure_data_studio_binary_location(), filename])
