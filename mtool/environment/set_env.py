import os
import sys
from mtool.cli import mtool

def set_env(args):
    m = mtool.MTool(args)
    m.set_env()
