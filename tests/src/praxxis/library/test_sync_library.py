"""
this tests the sync library functionality of praxxis
"""

import pytest 

def test_sync_library(setup, add_test_library, library_root, library_db, libraries_list, start, stop):
    """
    tests sync_library functionality. Requires that setup is run and the test notebooks are added.
    """
    from src.praxxis.library import sync_library
    from src.praxxis.library import list_library
    from tests.src.praxxis.util import dummy_object
    import os

    sync_library.sync_library(library_root, library_db)
        
    assert set(libraries_list) == set(*list_library.list_library(library_db, start, stop))