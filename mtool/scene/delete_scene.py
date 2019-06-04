import os
import sys

from mtool.cli import mtool

def delete_scene(args):
    m = mtool.MTool(args)
    name = m.delete_scene()
    m.log.info("New Current Scene", name)