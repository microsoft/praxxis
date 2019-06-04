import os
import sys

from mtool.cli import mtool

m = mtool.MTool(sys.argv)

m.delete_env()