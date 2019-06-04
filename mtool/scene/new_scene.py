import os
import sys

from mtool.cli import mtool

m = mtool.MTool(sys.argv)

name = m.create_scene()

m.log.header("Scene Created", name)
m.log.info("New Current Scene", name)