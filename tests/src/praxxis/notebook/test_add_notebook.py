def test_add_notebook(setup, library_db, current_scene_db, start, stop):
    from src.praxxis.notebook import add_notebook
    from src.praxxis.notebook import remove_notebook
    from tests.src.praxxis.util import dummy_object
    from src.praxxis.notebook import list_notebook
    
    dummy_notebook_path = dummy_object.make_dummy_notebook_path()
    dummy_notebook = dummy_object.make_dummy_notebook()

    add_notebook.add_notebook(dummy_notebook_path, library_db)
    assert len(list_notebook.list_notebook(library_db, current_scene_db, start, stop)) == 1

    remove_notebook.remove_notebook(dummy_notebook, library_db, current_scene_db)
    assert len(list_notebook.list_notebook(library_db, current_scene_db, start, stop)) == 0