def test_search_notebook(setup, setup_sqlite, add_test_library, library_db, current_scene_db, start, stop):
    import argparse
    from src.mtool.notebook import search_notebook

    namespace = argparse.Namespace
    namespace.term = 'DIR'

    notebooks = search_notebook.search_notebook(namespace, library_db, current_scene_db, start, stop)
    assert len(notebooks) == 2


##TODO: add test for notebook returning 0 results
def test_search_notebook_fail():
    pass