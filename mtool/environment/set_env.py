"""
This file calls the function to set an environment variable for the current
    scence (a value passed on the command line)

Dependencies within mtool: mtool/mtool.py
"""

import os
import sys

from mtool.cli import mtool

def set_env(args):
    m = mtool.MTool(args)
    m.set_env()
