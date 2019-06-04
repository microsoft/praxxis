
"""
This file calls the function to resume a previously used scene.

Dependencies within mtool: mtool/mtool.py
"""

import os
import sys

from mtool.cli import mtool

def resume_scene(args):
    m = mtool.MTool(args)
    name = m.resume_scene()
    m.log.info("Current Scene resumed", name)