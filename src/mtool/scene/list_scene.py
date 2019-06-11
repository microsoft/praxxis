"""
This file calls a function to list all scenes.

Dependencies within mtool: mtool/mtool.py
"""

import os
import sys

from src.mtool.cli import mtool

def list_scene(args):
    """Lists all scenes"""
    m = mtool.Mtool(args)
    m.log.header("Scenes")
    m.list_scenes()