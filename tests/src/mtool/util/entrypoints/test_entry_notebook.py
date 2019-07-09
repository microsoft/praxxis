from src.mtool.util.entrypoints import entry_notebook
from tests.src.mtool.util import dummy_object

def test_init_outfile(setup, outfile_root):
    import shutil 
    import os 

    assert os.path.exists(outfile_root)
    shutil.rmtree(outfile_root)
    assert not os.path.exists(outfile_root)

    entry_notebook.init_outfile(outfile_root)

    assert os.path.exists(outfile_root)

def test_next_notebook():    
    notebook = dummy_object.make_dummy_notebook()
    assert entry_notebook.next_notebook(notebook) == "coming soon"
def test_list_notebook(setup, add_test_library, scene_root, history_db, library_root, library_db, start, stop, current_scene_db):
    notebook = dummy_object.make_dummy_notebook()

    notebook_list = entry_notebook.list_notebook(notebook, scene_root, history_db, library_root, library_db, start, stop, current_scene_db)
    assert len(notebook_list) == 3

def test_search_notebook(setup, add_test_library, scene_root, history_db, library_db, start, stop, current_scene_db):
    search = dummy_object.make_dummy_search()

    notebooks = entry_notebook.search_notebook(search, scene_root, history_db, library_db, start, stop, current_scene_db)
    assert len(notebooks) == 2


def test_open_notebook(setup, add_test_library, scene_root, history_db, library_db, ads_location, current_scene_db):
    notebook = dummy_object.make_dummy_notebook()

    assert entry_notebook.open_notebook(notebook, scene_root, history_db, library_db, ads_location, current_scene_db) == 0


def test_run_notebook(setup, telemetry_db, outfile_root, library_root, library_db, scene_root, history_db, current_scene_db):
    notebook = dummy_object.make_dummy_notebook()

    assert entry_notebook.run_notebook(notebook, telemetry_db, outfile_root, library_root, library_db, scene_root, history_db, current_scene_db) == 0
