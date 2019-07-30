from src.praxxis.entrypoints import entry_notebook
from tests.src.praxxis.util import dummy_object

def test_init_outfile(setup, outfile_root):
    from tests.src.praxxis.util import rmtree
    import os 

    assert os.path.exists(outfile_root)
    rmtree.rmtree(outfile_root)
    assert not os.path.exists(outfile_root)

    entry_notebook.init_outfile(outfile_root)

    assert os.path.exists(outfile_root)

"""
def test_next_notebook():    
    notebook = dummy_object.make_dummy_notebook()
    assert entry_notebook.next_notebook(notebook) == "coming soon"
"""

def test_list_notebook(setup, add_test_library, scene_root, history_db, library_root, library_db, start, stop, current_scene_db):
    from src.praxxis.notebook import list_notebook
    notebook = dummy_object.make_dummy_notebook()

    entry_notebook.list_notebook(notebook, scene_root, history_db, library_root, library_db, start, stop, current_scene_db)
    assert len(list_notebook.list_notebook(library_db,current_scene_db, start, stop)) == 3


def test_search_notebook(setup, add_test_library, scene_root, history_db, library_db, start, stop, current_scene_db):
    from src.praxxis.notebook import search_notebook
    search = dummy_object.make_dummy_search()

    entry_notebook.search_notebook(search, scene_root, history_db, library_db, start, stop, current_scene_db)
    notebooks = search_notebook.search_notebook(search, library_db, current_scene_db, start, stop)
    assert len(notebooks) == 2


def test_open_notebook(setup, add_test_library, scene_root, history_db, library_db, ads_location, current_scene_db,):
    notebook = dummy_object.make_dummy_notebook()
    from src.praxxis.util import error
    try:
        entry_notebook.open_notebook(notebook, scene_root, history_db, library_db, ads_location, current_scene_db)
    except error.EditorNotFoundError:
        assert 1
    except error.ADSNotFoundError:
        assert 1
    except Exception:
        assert 0
    else:
        assert 1


def test_run_notebook(setup, add_test_library, telemetry_db, outfile_root, library_root, library_db, scene_root, history_db, current_scene_db):
    import os
    from src.praxxis.sqlite import sqlite_scene
    from src.praxxis.scene import history

    notebook = dummy_object.make_dummy_notebook()
    entry_notebook.run_notebook(notebook, telemetry_db, outfile_root, library_root, library_db, scene_root, history_db, current_scene_db)
    assert len(history.history(history_db, library_db, current_scene_db)) == 1
    sqlite_scene.clear_history(current_scene_db)


