import os
import sys

from mtool.cli import mtool

def new_scene(args):
    m = mtool.MTool(args)

    name = m.create_scene()

    m.log.header("Scene Created", name)
    m.log.info("New Current Scene", name)
