"""
This file calls the function to list all environment variables.

Dependencies within mtool: mtool/mtool.py
"""

import os
import sys

from mtool.cli import mtool

def list_env(args):
    m = mtool.MTool(args)
    m.log.header("Environment variables for all libraries")
    m.list_env()    
    