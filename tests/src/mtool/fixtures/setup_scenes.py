import pytest

@pytest.fixture(scope="function")
def create_many_scenes(scene_root, history_db, current_scene_db):
    from src.mtool.scene import new_scene
    from src.mtool.scene import delete_scene
    from tests.src.mtool.util import dummy_name_object

    name1 = dummy_name_object.make_dummy_object("generated_scene_1")

    name2 = dummy_name_object.make_dummy_object("generated_scene_2")

    new_scene.new_scene(name1, scene_root, history_db)
    new_scene.new_scene(name2, scene_root, history_db)
    yield
    delete_scene.delete_scene(name1, scene_root, history_db)
    delete_scene.delete_scene(name2, scene_root, history_db)


@pytest.fixture(scope="function")
def create_one_scene(scene_root, history_db, current_scene_db):
    from src.mtool.scene import new_scene
    from src.mtool.scene import delete_scene
    from tests.src.mtool.util import dummy_name_object

    name1 = dummy_name_object.make_dummy_object("generated_one_scene")
    new_scene.new_scene(name1, scene_root, history_db)
    yield 
    delete_scene.delete_scene(name1, scene_root, history_db)

@pytest.fixture(scope="function")
def create_ended_scene(scene_root, history_db, current_scene_db):
    from src.mtool.scene import new_scene
    from src.mtool.scene import delete_scene
    from src.mtool.scene import end_scene
    from tests.src.mtool.util import dummy_name_object

    name1 = dummy_name_object.make_dummy_object("generated_ended_scene")
    new_scene.new_scene(name1, scene_root, history_db)
    end_scene.end_scene(name1, scene_root, history_db, current_scene_db)
    yield 
    delete_scene.delete_scene(name1, scene_root, history_db)


@pytest.fixture(scope="function")
def generate_short_history(setup, add_test_library, init_root, outfile_root, current_scene_db, library_root, library_db):
    from src.mtool.notebook import run_notebook
    from tests.src.mtool.util import dummy_name_object

    notebook1 = dummy_name_object.make_dummy_notebook("DIR001 - dir")
    run_notebook.run_notebook(notebook1, init_root, outfile_root, current_scene_db, library_root, library_db)

