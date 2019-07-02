"""
this tests the sync library functionality of mtool
"""

import pytest 

def test_sync_library(setup, add_test_library, library_root, library_db, libraries_list):
    """
    tests sync_library functionality. Requires that setup is run and the test notebooks are added.
    """
    from src.mtool.library import sync_library
    from src.mtool.library import list_library

    sync_library.sync_libraries(library_root, library_db)
    
    assert set(libraries_list) == set(*list_library.list_library(library_root, library_db))
