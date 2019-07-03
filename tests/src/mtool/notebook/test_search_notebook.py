def test_search_notebook(setup, add_test_library, library_db, current_scene_db, start, stop):
    import argparse
    from src.mtool.notebook import search_notebook
    from tests.src.mtool.util import dummy_name_object

    term = dummy_name_object.make_dummy_object("", "", "DIR")

    notebooks = search_notebook.search_notebook(term, library_db, current_scene_db, start, stop)
    assert len(notebooks) == 2


##TODO: add test for notebook returning 0 results
def test_search_notebook_fail():
    pass