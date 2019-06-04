"""
This file calls a function to change the current scene.

Dependencies within mtool: mtool/mtool.py
"""

import os
import sys

from mtool.cli import mtool

def change_scene(args):
    m = mtool.MTool(args)

    name = m.set_scene()
    m.log.info("New Current Scene", name)