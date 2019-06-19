from src.mtool.notebook import list_notebook

def test_list_notebook(scene_root, library_db, current_scene_db, start, stop):
    list_notebook.list_notebook(scene_root, library_db, current_scene_db, start, stop)