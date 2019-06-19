from src.mtool.library import list_library

def test_list_library(library_root, library_db, current_scene_db):
    list_library.list_library(library_root, library_db, current_scene_db)
