import os
import sys

from mtool.cli import mtool

m = mtool.MTool(sys.argv)

name = m.set_scene()
m.log.info("New Current Scene", name)