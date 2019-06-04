import os
import sys
import shutil
import subprocess

from mtool.cli import mtool

m = None

def open_notebook(args):
    global m
    m = mtool.MTool(args)
    m.set_environment_overrides_for_scene()
    m.for_each_notebook_specified_on_command_line(load_notebook)


def load_notebook(filename):

    notebook = m.notebook(filename)
    outputfile = notebook.get_local_copy_filename('.ipynb')
    shutil.copyfile(filename, outputfile)
    subprocess.Popen([m.azure_data_studio_binary_location, outputfile])
