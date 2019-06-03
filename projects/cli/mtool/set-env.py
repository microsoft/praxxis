"""
This file calls the function to set an environment variable for the current
    scence (a value passed on the command line)

Dependencies within mtool: mtool/mtool.py
"""
import os
import sys

# Include the mtool subfolder folder
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), "mtool"))

import mtool

m = mtool.MTool(sys.argv)

m.set_env()