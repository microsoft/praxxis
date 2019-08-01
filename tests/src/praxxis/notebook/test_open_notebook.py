import pytest
import sys

@pytest.mark.skipif(sys.platform == "darwin", reason="ADS can be installed in a bunch of places on macos")
def test_open_notebook_ads(setup, add_test_library, current_scene_db, library_db, ads_location):
    from src.praxxis.notebook import open_notebook
    from tests.src.praxxis.util import dummy_object
    from src.praxxis.util import error
    from src.praxxis.display import display_error

    notebook1 = dummy_object.make_dummy_notebook(viewer="ads")
    try:
        assert open_notebook.open_notebook(notebook1, current_scene_db, library_db, ads_location, test=True) == 0
    except error.ADSNotFoundError as e:
        assert str(e) == display_error.ads_not_found_error(ads_location)


@pytest.mark.skipif(sys.platform == "darwin", reason="ADS can be installed in a bunch of places on macos")
def test_open_notebook_ads_not_found(setup, add_test_library, current_scene_db, library_db):
    from src.praxxis.notebook import open_notebook
    from tests.src.praxxis.util import dummy_object
    from src.praxxis.util import error
    from src.praxxis.display import display_error

    notebook1 = dummy_object.make_dummy_notebook(viewer="ads")
    ads_location = "fake_path"
    try:
        assert open_notebook.open_notebook(notebook1, current_scene_db, library_db, ads_location, test=True) == 0
        assert 0 # previous command should fail
    except error.ADSNotFoundError as e:
        assert str(e) == display_error.ads_not_found_error(ads_location)


def test_open_notebook_html(setup, add_test_library, current_scene_db, library_db, ads_location):
    from src.praxxis.notebook import open_notebook
    from tests.src.praxxis.util import dummy_object

    notebook1 = dummy_object.make_dummy_notebook(viewer="html")
    assert open_notebook.open_notebook(notebook1, current_scene_db, library_db, ads_location, True) == 0

def test_open_notebook_bad_editor(setup, add_test_library, current_scene_db, library_db, ads_location):
    from src.praxxis.notebook import open_notebook
    from tests.src.praxxis.util import dummy_object
    from src.praxxis.util import error
    from src.praxxis.display import display_error

    notebook1 = dummy_object.make_dummy_notebook()
    editor = "not real"
    try:
        open_notebook.open_notebook(notebook1, current_scene_db, library_db, ads_location, editor, test=True) == 0
        assert 0
    except error.EditorNotFoundError as e:
        assert str(e) == display_error.editor_not_found_error(editor)

def test_open_notebook_editor(setup, add_test_library, current_scene_db, library_db, ads_location):
    from src.praxxis.notebook import open_notebook
    from tests.src.praxxis.util import dummy_object
    from src.praxxis.util import error
    from src.praxxis.display import display_error

    notebook1 = dummy_object.make_dummy_notebook()
    editor = "vim"
    try:
        assert open_notebook.open_notebook(notebook1, current_scene_db, library_db, ads_location, editor, test=True) == 0
    except error.EditorNotFoundError as e:
        # if vim not installed (e.g. windows)
        assert str(e) == display_error.editor_not_found_error(editor)

def test_open_notebook_jupyter(setup, add_test_library, current_scene_db, library_db, ads_location):
    from src.praxxis.notebook import open_notebook
    from tests.src.praxxis.util import dummy_object
    from src.praxxis.util import error

    notebook1 = dummy_object.make_dummy_notebook(viewer="jupyter")
    assert open_notebook.open_notebook(notebook1, current_scene_db, library_db, ads_location, test=True) == 0
    