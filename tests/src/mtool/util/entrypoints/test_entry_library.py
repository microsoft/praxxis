from src.mtool.util.entrypoints import entry_library

def test_init_library(setup, library_root, library_db):
    import shutil 
    import os 
    
    assert os.path.exists(library_root)
    assert os.path.exists(library_db)
    shutil.rmtree(library_root)
    assert not os.path.exists(library_root)
    
    entry_library.init_library(library_root, library_db)
    
    assert os.path.exists(library_root)
    assert os.path.exists(library_db)


def test_sync_library(setup, library_root, library_db):
    libraries = entry_library.sync_library("", library_root, library_db)
    assert libraries == 0


def test_list_library(setup, add_test_library, library_root, library_db):
    libraries = entry_library.list_library("", library_root, library_db)
    assert len(libraries) == 1


def test_add_library():
    assert entry_library.add_library("") == "coming soon"

