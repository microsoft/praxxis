from src.mtool.library import load_library

def test_load_libraries(library_root, library_db):
    load_library.load_libraries(library_root, library_db)


def test_load_library(library_root, library_db):
    load_library.load_library(library_root, library_db)


def test_load_notebooks(library_root, library_db, library_name):
    load_library.load_notebooks(library_root, library_db, library_name)