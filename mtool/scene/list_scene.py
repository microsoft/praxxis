import os
import sys

from mtool.cli import mtool

def list_scene(args):
    m = mtool.MTool(args)
    m.log.header("Scenes")
    m.list_scenes()