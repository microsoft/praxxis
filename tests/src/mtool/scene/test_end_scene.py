def test_end_scene_success(setup, create_one_scene, scene_root, history_db, current_scene_db):
    from src.mtool.scene import end_scene
    from tests.src.mtool.util import dummy_object
    name1 = dummy_object.make_dummy_scene("generated_one_scene")

    message = end_scene.end_scene(name1, scene_root, history_db, current_scene_db)
    assert message == "success"

def test_end_scene_failure(setup, scene_root, history_db, current_scene_db):
    from src.mtool.scene import end_scene
    from tests.src.mtool.util import dummy_object
    name1 = dummy_object.make_dummy_scene("nonexistent_scene")

    message = end_scene.end_scene(name1, scene_root, history_db, current_scene_db)
    assert message == "scene_not_exist"
