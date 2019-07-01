import pytest
import os

@pytest.fixture(scope="session")
def init_root(tmpdir_factory):
    return tmpdir_factory.mktemp('mtool')

@pytest.fixture(scope="session")
def scene_root(init_root):
    return os.path.join(init_root, "test_scene")


@pytest.fixture(scope="session")
def library_root(init_root):
    return os.path.join(init_root, "test_library")


@pytest.fixture(scope="session")
def library_db(library_root):
    return os.path.join(library_root, "test_library")


@pytest.fixture(scope="session")
def outfile_root(init_root):
    return os.path.join(init_root, "test_output")


@pytest.fixture(scope="session")
def history_db(init_root):
    return os.path.join(init_root, "current_scene.db")


@pytest.fixture(scope="session")
def telemetry_db(init_root):
    return os.path.join(init_root, "user_id.db")

@pytest.fixture(scope="session")
def default_scene_name():
    return "scene"


@pytest.fixture(scope="session")
def setup(init_root, library_root, library_db, outfile_root, scene_root, history_db, default_scene_name, ):
    from src.mtool.util.sqlite import sqlite_library
    from src.mtool.util.sqlite import sqlite_scene
    from tests.src.mtool.util.sqlite import test_sqlite_scene
    from tests.src.mtool.util.sqlite import test_sqlite_library
    from tests.src.mtool.scene import test_new_scene
    from tests.src.mtool.scene import test_scene

    if not os.path.exists(init_root):
        os.mkdir(init_root)
        assert os.path.exists(init_root)

    if not os.path.exists(library_root):
        os.mkdir(library_root)
        assert os.path.exists(library_root)

    if not os.path.exists(library_db):
        sqlite_library.init_library_db(library_db)
        assert os.path.exists(library_db)
    
    if not os.path.exists(outfile_root):
        os.mkdir(outfile_root)
        assert os.path.exists(outfile_root)

    if not os.path.exists(scene_root):
        os.mkdir(scene_root)
        assert os.path.exists(scene_root)
    
    if not os.path.exists(history_db):
        sqlite_scene.init_current_scene(history_db, default_scene_name)
        assert os.path.exists(history_db)


@pytest.fixture (scope="session")
def setup_sqlite(setup, library_db):
        from tests.src.mtool.util.sqlite import test_sqlite_library
        from tests.src.mtool.scene import test_new_scene
        from tests.src.mtool.util.sqlite import test_sqlite_scene
        from tests.src.mtool.scene import test_scene

        test_sqlite_library.test_init_library_db(setup, library_db)
        scene_db = test_new_scene.test_new_scene(setup, init_root, default_scene_name, scene_root, history_db)
        test_scene.init_scene(init_root, history_db, default_scene_name, scene_db)
        test_sqlite_scene.init_scene_db(setup, scene_db)


