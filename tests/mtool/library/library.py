from src.mtool.library import library

def test_init_library(library_root, library_db):
    library.init_library(library_root, library_db)