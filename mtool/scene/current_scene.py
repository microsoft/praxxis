import os
import sys

from mtool.cli import mtool

def current_scene(args):
    m = mtool.MTool(args)
    m.set_environment_overrides_for_scene()