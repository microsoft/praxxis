import os
import sys
from mtool.cli import mtool

def resume_scene(args):
    m = mtool.MTool(args)

    name = m.resume_scene()
    m.log.info("Current Scene resumed", name)