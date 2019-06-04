"""
This file sets up the toml overrides for the current scene.

Dependencies within mtool: mtool/mtool.py
"""

import os
import sys

from mtool.cli import mtool

def current_scene(args):
    m = mtool.MTool(args)
    m.set_environment_overrides_for_scene()