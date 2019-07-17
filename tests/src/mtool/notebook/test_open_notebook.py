def test_open_notebook_ads(setup, add_test_library, current_scene_db, library_db, ads_location):
    from src.mtool.notebook import open_notebook
    from tests.src.mtool.util import dummy_object

    notebook1 = dummy_object.make_dummy_notebook(environment="ads")
    assert open_notebook.open_notebook(notebook1, current_scene_db, library_db, ads_location, True) == 0


def test_open_notebook_html(setup, add_test_library, current_scene_db, library_db, ads_location):
    from src.mtool.notebook import open_notebook
    from tests.src.mtool.util import dummy_object

    notebook1 = dummy_object.make_dummy_notebook(environment="html")
    assert open_notebook.open_notebook(notebook1, current_scene_db, library_db, ads_location, True) == 0
