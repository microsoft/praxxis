"""
This file opens a notebook in Azure Data Studio.

Dependencies within mtool: mtool/mtool.py
"""

import os
import sys
import shutil
import subprocess

from src.mtool.cli import mtool

m = None

def open_notebook(args):
    """Open a notebook"""
    global m
    m = mtool.MTool(args)
    m.set_environment_overrides_for_scene()


def load_notebook(filename):
    """Opens a notebook in Azure Data Studio

    Keyword arguments:
    filename -- name of notebook to open
    """
