from src.mtool.util.entrypoints import entry_scene
from tests.src.mtool.util import dummy_object

def test_init_scene(setup, scene_root, history_db, default_scene_name):
    from src.mtool.util import rmtree
    import os 

    assert os.path.exists(scene_root)
    assert os.path.exists(history_db)
    rmtree.rmtree(scene_root)
    os.remove(history_db)
    assert not os.path.exists(scene_root)
    
    entry_scene.init_scene(scene_root, history_db, default_scene_name)

    assert os.path.exists(scene_root)

def test_delete_scene(setup, create_one_scene, scene_root, history_db):
    from src.mtool.scene import list_scene
    entry_scene.delete_scene("generated_one_scene", scene_root, history_db)

    assert len(list_scene.list_scene(scene_root, history_db)) == 1

    
def test_resume_scene(setup, create_ended_scene, scene_root, history_db):
    from src.mtool.util.sqlite import sqlite_scene
    from src.mtool.util import error

    entry_scene.resume_scene("generated_ended_scene", scene_root, history_db)
    try:
        sqlite_scene.check_scene_ended(history_db, "generated_ended_scene")
    except Exception:
        assert 0
    else:
        assert 1



def test_change_scene(setup, create_one_scene, scene_root, history_db):
    from src.mtool.scene import current_scene

    scene = dummy_object.make_dummy_scene("scene")
    
    entry_scene.change_scene(scene, scene_root, history_db)
    current_scene = current_scene.current_scene(scene_root, history_db)

    assert current_scene == "scene"


def test_end_scene(setup, create_one_scene, scene_root, history_db, current_scene_db):
    from src.mtool.scene import list_scene
    from src.mtool.util.sqlite import sqlite_scene
    from src.mtool.util import error

    entry_scene.end_scene("generated_one_scene", scene_root, history_db, current_scene_db)

    try:
        sqlite_scene.check_scene_ended(history_db, "generated_one_scene")
    except error.SceneEndedError:
        assert 1
    else:
        assert 0


def test_new_scene(setup, scene_root, history_db):
    from src.mtool.scene import delete_scene
    from src.mtool.scene import current_scene

    scene = dummy_object.make_dummy_scene("generated_new_scene")

    entry_scene.new_scene(scene, scene_root, history_db)
    current_scene = current_scene.current_scene(scene_root, history_db)

    assert current_scene == "generated_new_scene"

    delete_scene.delete_scene("generated_new_scene", scene_root, history_db)


def test_history(setup, generate_short_history, scene_root, history_db, library_db, current_scene_db):
    from src.mtool.scene import history
    entry_scene.history("", scene_root, history_db, library_db, current_scene_db)
    history = history.history(history_db, library_db, current_scene_db)

    assert len(history) == 1

