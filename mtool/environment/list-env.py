import os
import sys

from mtool.cli import mtool

m = mtool.MTool(sys.argv)
m.log.header("Environment variables for all libraries")
m.list_env()
