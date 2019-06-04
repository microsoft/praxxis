import os
import sys

from mtool.cli import mtool

def end_scene(args):
    m = mtool.MTool(args)
    m.log.info("Current Scene ended", m.end_scene())