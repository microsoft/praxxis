import os
import sys

from mtool.cli import mtool

m = mtool.MTool(sys.argv)

m.set_environment_overrides_for_scene()