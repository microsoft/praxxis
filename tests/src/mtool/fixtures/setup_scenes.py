import pytest

@pytest.fixture(scope="function")
def create_many_scenes(scene_root, history_db, current_scene_db, default_scene_name):
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

