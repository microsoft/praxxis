import os
import sys

from mtool.cli import mtool

def list_scenes(args):
    m = mtool.MTool(args)

    m.log.header("Scenes")
    m.list_scenes()