from src.praxxis.entrypoints import entry_library
import pytest
import sys

def test_init_library(setup, library_root, library_db):
    from src.praxxis.util import rmtree
    import os 
    
    assert os.path.exists(library_root)
    assert os.path.exists(library_db)
    rmtree.rmtree(library_root)
    assert not os.path.exists(library_root)
    
    entry_library.init_library(library_root, library_db)
    
    assert os.path.exists(library_root)
    assert os.path.exists(library_db)


def test_sync_library(setup, library_root, library_db, start, stop):
    from src.praxxis.library import list_library

    entry_library.sync_library("", library_root, library_db)
    libraries = list_library.list_library(library_db, start, stop)
    assert len(libraries) == 0


def test_list_library(setup, add_test_library, library_db, start, stop):
    from src.praxxis.library import list_library
    entry_library.list_library("", library_db)
    assert len(list_library.list_library(library_db, start, stop)) == 1


@pytest.mark.skipif(sys.platform != "linux", reason="will fail test on windows until git integration is merged")
def test_add_library(setup, library_db ,start, stop): 
    from src.praxxis.util import error
    from tests.src.praxxis.util import dummy_object
    from src.praxxis.library import remove_library
    from src.praxxis.library import list_library

    dummy_library = dummy_object.make_dummy_library_path()
    entry_library.add_library(dummy_library, library_db)
    assert len(list_library.list_library(library_db, start, stop)) == 1

    remove_library.remove_library(dummy_library, library_db, start, stop)
