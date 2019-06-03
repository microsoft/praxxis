"""
This file opens a notebook in Azure Data Studio.

Dependencies within mtool: mtool/mtool.py
"""
import os
import sys
import shutil
import subprocess

# Include the mtool subfolder folder
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), "mtool"))

import mtool

m = mtool.MTool(sys.argv)

def load_notebook(filename):
    """Opens a notebook in Azure Data Studio

    Keyword arguments:
    filename -- name of notebook to open
    """
    notebook = m.notebook(filename)
    outputfile = notebook.get_local_copy_filename('.ipynb')
    shutil.copyfile(filename, outputfile)
    subprocess.Popen([m.azure_data_studio_binary_location, outputfile])

m.set_environment_overrides_for_scene()
m.for_each_notebook_specified_on_command_line(load_notebook)
