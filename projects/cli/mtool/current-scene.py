"""
This file sets up the toml overrides for the current scene.

Dependencies within mtool: mtool/mtool.py
"""
import os
import sys

# Include the mtool subfolder folder
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), "mtool"))

import mtool

m = mtool.MTool(sys.argv)

m.set_environment_overrides_for_scene()