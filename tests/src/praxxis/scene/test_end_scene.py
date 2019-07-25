def test_end_scene_success(setup, create_one_scene, scene_root, history_db, current_scene_db):
    from src.praxxis.scene import end_scene
    from tests.src.praxxis.util import dummy_object
    name1 = dummy_object.make_dummy_scene("generated_one_scene")

    message = end_scene.end_scene(name1, scene_root, history_db, current_scene_db)
    assert message == "generated_one_scene"

def test_end_scene_failure(setup, scene_root, history_db, current_scene_db):
    from src.praxxis.scene import end_scene
    from tests.src.praxxis.util import dummy_object
    from src.praxxis.util import error
    from src.praxxis.display import display_error


    name1 = dummy_object.make_dummy_scene("nonexistent_scene")

    try:
        end_scene.end_scene(name1, scene_root, history_db, current_scene_db)
    except error.SceneNotFoundError as e:
        assert str(e) == display_error.scene_not_found_error(name1.name)

def test_end_scene_ended(setup, scene_root, history_db, current_scene_db, create_ended_scene):
    from src.praxxis.scene import end_scene
    from tests.src.praxxis.util import dummy_object
    from src.praxxis.util import error
    from src.praxxis.display import display_error

    name1 = dummy_object.make_dummy_scene("generated_ended_scene")

    try:
        end_scene.end_scene(name1, scene_root, history_db, current_scene_db)
    except error.EndEndedSceneError as e:
        assert str(e) == display_error.end_ended_scene_error(name1.name)

def test_end_scene_last_active(setup, scene_root, history_db, current_scene_db):
    from src.praxxis.scene import end_scene
    from tests.src.praxxis.util import dummy_object
    from src.praxxis.util import error
    from src.praxxis.display import display_error

    name1 = dummy_object.make_dummy_scene("scene")

    try:
        end_scene.end_scene(name1, scene_root, history_db, current_scene_db)
        assert 0
    except error.LastActiveSceneError as e:
        assert str(e) == display_error.last_active_scene_error(name1.name)