import os
import sys

from mtool.cli import mtool

m = mtool.MTool(sys.argv)

name = m.delete_scene()

m.log.info("New Current Scene", name)