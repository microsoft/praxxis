import os
import sys

from mtool.cli import mtool

m = mtool.MTool(sys.argv)
m.log.info("Current Scene ended", m.end_scene())