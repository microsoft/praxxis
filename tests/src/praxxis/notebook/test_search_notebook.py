def test_search_notebook(setup, add_test_library, library_db, current_scene_db, start, stop):
    import argparse
    from src.praxxis.notebook import search_notebook
    from tests.src.praxxis.util import dummy_object

    term = dummy_object.make_dummy_search()

    notebooks = search_notebook.search_notebook(term, library_db, current_scene_db, start, stop)
    assert len(notebooks) == 2


##TODO: add test for notebook returning 0 results
def test_search_notebook_fail():
    pass