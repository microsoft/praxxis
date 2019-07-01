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
    print()
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
