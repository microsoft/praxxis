"""
This file calls the function to delete an environment variable.

Dependencies within mtool: mtool/mtool.py
"""

import os
import sys

from src.mtool.cli import mtool

def delete_env(args):
    """Calls the Mtool method delete environment"""
    m = mtool.MTool(args)
    m.delete_env()