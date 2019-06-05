"""
This file calls the function to create a new scene.

Dependencies within mtool: mtool/mtool.py
"""

import os
import sys

from mtool.cli import mtool

def new_scene(args):
    """Creates new scene"""
    m = mtool.MTool(args)
    name = m.create_scene()
    m.log.header("Scene Created", name)
    m.log.info("New Current Scene", name)
