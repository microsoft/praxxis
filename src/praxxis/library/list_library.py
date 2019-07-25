"""
This file prints a list of all notebook libraries installed on this machine.
"""

def list_library(library_db, start, stop):
    """grabs the list of libraries from the libraries db, and displays through 
    its display function"""
    from src.praxxis.sqlite import sqlite_library
    from src.praxxis.display import display_library
    
    libraries = sqlite_library.list_libraries(library_db, start, stop)
    display_library.display_libraries(libraries)
    return libraries
