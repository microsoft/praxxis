"""
This file sets up the toml overrides for the current scene.

Dependencies within mtool: mtool/mtool.py
"""

import os
import sys

from src.mtool.cli import mtool

def current_scene(args):
    """Sets up environment for current scene"""
    m = mtool.Mtool(args)
    m.set_environment_overrides_for_scene()