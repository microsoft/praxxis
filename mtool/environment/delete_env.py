"""
This file calls the function to delete an environment variable.

Dependencies within mtool: mtool/mtool.py
"""

import os
import sys

from mtool.cli import mtool

def delete_env(args):
    m = mtool.MTool(args)
    m.delete_env()