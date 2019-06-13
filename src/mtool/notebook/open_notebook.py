"""
This file opens a notebook in Azure Data Studio.

Dependencies within mtool: notebook.py, scene.py
"""

import os
import sys
import shutil
import subprocess

import pypandoc
import webbrowser
#TODO: the version of pandoc that's on wheel is ... ugly and doesn't support ipynb

from src.mtool.notebook.notebook import Notebook

def open_notebook(args, scene_root):
    from src.mtool.util import sqlite_util
    """Open a notebook"""
    # notebook = the number of the notebook
    history_db = os.path.join(scene_root, "current_scene.db")
    db_file = os.path.join(scene_root, sqlite_util.get_current_scene(history_db), sqlite_util.get_current_scene(history_db) + ".db")
    notebook_filename = sqlite_util.ordinal_to_list_item(db_file, args.notebook)[0]
    display_in_editor(notebook_filename)

def azure_data_studio_binary_location():
    ##TODO: THIS IS WINDOWS SPECIFIC
    """Returns location of ADS binary"""
    return os.path.join(os.getenv('LOCALAPPDATA'), 'Programs', 'Azure Data Studio', 'azuredatastudio')

def display_as_html(html_outputfile):
    webbrowser.open(html_outputfile)

def get_html_result(filename, html_outputfile):
    pypandoc.convert_file(filename, 'html', outputfile=html_outputfile)
    return html_outputfile

def display_in_editor(filename):
    """Opens a notebook in Azure Data Studio

    Keyword arguments:
    filename -- name of notebook to open
    """
    subprocess.Popen([azure_data_studio_binary_location(), filename])
