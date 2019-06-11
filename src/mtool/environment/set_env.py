"""
This file calls the function to set an environment variable for the current
    scence (a value passed on the command line)

Dependencies within mtool: mtool/mtool.py
"""

import os
import sys

from src.mtool.cli import mtool

def set_env(args):
    """Call mtool method to set environment variables"""
    m = mtool.Mtool(args)
    m.set_env()
