import pytest

@pytest.fixture(scope="function")
def create_many_scenes(scene_root, history_db, current_scene_db):
    from src.praxxis.scene import new_scene
    from src.praxxis.scene import delete_scene
    from tests.src.praxxis.util import dummy_object
    from src.praxxis.util import error

    name1 = dummy_object.make_dummy_scene("generated_scene_1")

    name2 = dummy_object.make_dummy_scene("generated_scene_2")

    new_scene.new_scene(name1, scene_root, history_db)
    new_scene.new_scene(name2, scene_root, history_db)
    yield
    try:
        delete_scene.delete_scene(name1, scene_root, history_db)
        delete_scene.delete_scene(name2, scene_root, history_db)
    except error.SceneNotFoundError:
        pass


@pytest.fixture(scope="function")
def create_one_scene(scene_root, history_db, current_scene_db):
    from src.praxxis.scene import new_scene
    from src.praxxis.scene import delete_scene
    from tests.src.praxxis.util import dummy_object
    from src.praxxis.util import error

    name1 = dummy_object.make_dummy_scene("generated_one_scene")
    new_scene.new_scene(name1, scene_root, history_db)
    yield 
    try:
        delete_scene.delete_scene(name1, scene_root, history_db)
    except error.SceneNotFoundError:
        pass


@pytest.fixture(scope="function")
def create_ended_scene(scene_root, history_db, current_scene_db):
    from src.praxxis.scene import new_scene
    from src.praxxis.scene import delete_scene
    from src.praxxis.scene import end_scene
    from tests.src.praxxis.util import dummy_object
    from src.praxxis.util import error
    from src.praxxis.display import display_error

    name1 = dummy_object.make_dummy_scene("generated_ended_scene")
    new_scene.new_scene(name1, scene_root, history_db)
    end_scene.end_scene(name1, scene_root, history_db, current_scene_db)
    yield 
    try:
        delete_scene.delete_scene(name1, scene_root, history_db)
    except error.SceneNotFoundError:
        pass


@pytest.fixture(scope="function")
def generate_short_history(setup, add_test_library, telemetry_db, output_root, current_scene_db, library_root, library_db, query_start, query_end):
    from src.praxxis.notebook import run_notebook
    from tests.src.praxxis.util import dummy_object
    from src.praxxis.sqlite import sqlite_scene
    import os

    notebook1 = dummy_object.make_dummy_notebook()
    run_notebook.run_notebook(notebook1, telemetry_db, output_root, current_scene_db, library_root, library_db, query_start, query_end)
    yield 
    sqlite_scene.clear_history(current_scene_db)
