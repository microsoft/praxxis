"""
defines the fixture level roots that are used by the rest of the project
"""
import pytest
import os

@pytest.fixture(scope="session")
def init_root(tmpdir_factory):
    """
    inits the root directory for the project. Is a tempdir, and will be deleted once the tests finish
    """
    return tmpdir_factory.mktemp('mtool')


@pytest.fixture(scope="session")
def scene_root(init_root):
    """
    defines the scene directory for testing
    """
    return os.path.join(init_root, "test_scene")


@pytest.fixture(scope="session")
def library_root(init_root):
    """
    defines the library root for testing
    """
    return os.path.join(init_root, "test_library")


@pytest.fixture(scope="session")
def library_db(library_root):
    """
    defines the library database location
    """
    return os.path.join(library_root, "libraries.db")


@pytest.fixture(scope="session")
def outfile_root(init_root):
    """
    defines the test output folder location
    """
    return os.path.join(init_root, "test_output")


@pytest.fixture(scope="session")
def history_db(init_root):
    """
    defines the history database for testing
    """
    return os.path.join(init_root, "history.db")


@pytest.fixture(scope="session")
def telemetry_db(init_root):
    """
    defines the user id database for testing 
    """
    return os.path.join(init_root, "user_id.db")


@pytest.fixture(scope="session")
def prediction_root(init_root):
    """
    defines the prediction root 
    """
    return os.path.join(init_root, "prediction")


@pytest.fixture(scope="session")
def prediction_db(prediction_root):
    """
    defines the prediction db location 
    """
    return os.path.join(prediction_root, "prediction.db")


@pytest.fixture(scope="session")
def ads_location(init_root):
    """
    defines the ads location for opening
    """
    import sys
    if(sys.platform == "linux"):
        return os.path.join('/usr', 'share', 'azuredatastudio', 'azuredatastudio')
    else:
        return os.path.join(os.getenv('LOCALAPPDATA'), 'Programs', 'Azure Data Studio', 'azuredatastudio')



@pytest.fixture(scope="session")
def default_scene_name():
    """
    defines the default scene name for testing
    """
    return "scene"


@pytest.fixture(scope="session")
def current_scene_db(init_root, scene_root, history_db):
    from src.mtool.util import roots
    return roots.get_current_scene_db(scene_root, history_db)
    

@pytest.fixture(scope="session")
def start():
    return 0


@pytest.fixture(scope="session")
def stop():
    return 100

