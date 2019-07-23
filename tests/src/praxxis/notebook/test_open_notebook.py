def test_open_notebook_ads(setup, add_test_library, current_scene_db, library_db, ads_location):
    from src.praxxis.notebook import open_notebook
    from tests.src.praxxis.util import dummy_object
    from src.praxxis.util import error

    notebook1 = dummy_object.make_dummy_notebook(viewer="ads")
    try:
        assert open_notebook.open_notebook(notebook1, current_scene_db, library_db, ads_location, True) == 0
    except error.ADSNotFoundError:
        assert 1


def test_open_notebook_html(setup, add_test_library, current_scene_db, library_db, ads_location):
    from src.praxxis.notebook import open_notebook
    from tests.src.praxxis.util import dummy_object

    notebook1 = dummy_object.make_dummy_notebook(viewer="html")
    assert open_notebook.open_notebook(notebook1, current_scene_db, library_db, ads_location, True) == 0
