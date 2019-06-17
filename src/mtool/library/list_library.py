"""
This file prints a list of all notebook libraries installed on this machine.
"""

import os
import json

def list_library(library_root, library_db, current_scene_db):
    """grabs the list of libraries from the libraries db, and displays through 
    its display function"""
    from src.mtool.library import library
    from src.mtool.util import sqlite_util
    from src.mtool.cli import display
    
    library.init_library(library_root, library_db)
    libraries = sqlite_util.list_libraries(library_db, 0, 10)
    display.display_libraries(libraries)
