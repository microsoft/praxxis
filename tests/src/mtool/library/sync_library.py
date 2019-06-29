from src.mtool.library import sync_library

def test_load_libraries(library_root, library_db):
    sync_library.sync_libraries(library_root, library_db)


def test_sync_library(library_root, library_db):
    sync_library.sync_library(library_root, library_db)


def test_load_notebooks(library_root, library_db, library_name):
    sync_library.sync_notebooks(library_root, library_db, library_name)