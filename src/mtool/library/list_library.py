"""
This file prints a list of all notebook libraries installed on this machine.

Dependencies within mtool: mtool/mtool.py
"""
import os
import sys
import json

def list_library(library_root, library_db, current_scene_db):
        from src.mtool.library import library
        from src.mtool.util import sqlite_util
        from src.mtool.cli import display
        
        library.init_library(library_root, library_db)
        libraries = sqlite_util.list_libraries(library_db, 0, 10)
        sqlite_util.write_list(current_scene_db, libraries)
        display.display_libraries(libraries)


