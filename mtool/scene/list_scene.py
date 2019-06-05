"""
This file calls a function to list all scenes.

Dependencies within mtool: mtool/mtool.py
"""
import os
import sys

from mtool.cli import mtool

def list_scene(args):
    """Lists all scenes"""
    m = mtool.MTool(args)
    m.log.header("Scenes")
    m.list_scenes()