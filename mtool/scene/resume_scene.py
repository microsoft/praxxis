import os
import sys
from mtool.cli import mtool

m = mtool.MTool(sys.argv)
name = m.resume_scene()
m.log.info("Current Scene resumed", name)