"""
This file calls a function to change the current scene.

Dependencies within mtool: mtool/mtool.py
"""

import os
import sys

from src.mtool.cli import mtool

def change_scene(args):
    """Calls mtool method to change the current scene"""
    m = mtool.Mtool(args)

    name = m.set_scene()
    m.log.info("New Current Scene", name)