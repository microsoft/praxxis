"""
This file calls the function to end the current scence.

Dependencies within mtool: mtool/mtool.py
"""

import os
import sys

from mtool.cli import mtool

def end_scene(args):
    """Ends a scene"""
    m = mtool.MTool(args)
    m.log.info("Current Scene ended", m.end_scene())