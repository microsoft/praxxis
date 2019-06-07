"""
This file runs a notebook. Results are either printed to the console or 
opened as an html output in the web browser, depending on user input.

Dependencies within mtool: mtool/mtool.py
"""

import os
import sys
import webbrowser
from src.mtool.cli import mtool

m = None

def run_notebook(args):
    """Runs one or more notebooks specified"""
    global m
    m = mtool.MTool(args)
    m.set_environment_overrides_for_scene()


def run(filename):
    """Run a notebook.

    Keyword arguments:
    filename -- the name of a notebook to run
    Keyword exceptions:
    if notebook fails to execute correctly (raises error in running)
    """
    log = m.log
    spinner = m.spinner

    log.header("Running")


    spinner.start()
