import os
import sys

# Include the mtool subfolder folder
#
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), "mtool"))

import mtool

m = mtool.MTool(sys.argv)
name = m.resume_scene()
m.log.info("Current Scene resumed", name)