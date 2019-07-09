from src.mtool.util.entrypoints import entry_scene
from tests.src.mtool.util import dummy_object

def test_init_scene(setup, scene_root, history_db, default_scene_name):
    import shutil 
    import os 

    assert os.path.exists(scene_root)
    assert os.path.exists(history_db)
    shutil.rmtree(scene_root)
    os.remove(history_db)
    assert not os.path.exists(scene_root)
    
    entry_scene.init_scene(scene_root, history_db, default_scene_name)

    assert os.path.exists(scene_root)

def test_delete_scene(setup, create_one_scene, scene_root, history_db):
    delete_scene = entry_scene.delete_scene("generated_one_scene", scene_root, history_db)

    assert delete_scene == "generated_one_scene"

    
def test_resume_scene(setup, create_ended_scene, scene_root, history_db):
    resume_scene = entry_scene.resume_scene("generated_ended_scene", scene_root, history_db)

    assert resume_scene == "generated_ended_scene"


def test_change_scene(setup, create_one_scene, scene_root, history_db):
    scene = dummy_object.make_dummy_scene("scene")

    change_scene = entry_scene.change_scene(scene, scene_root, history_db)
    assert change_scene == "scene"


def test_end_scene(setup, create_one_scene, scene_root, history_db, current_scene_db):
    ended = entry_scene.end_scene("generated_one_scene", scene_root, history_db, current_scene_db)

    assert ended == "generated_one_scene"


def test_new_scene(setup, scene_root, history_db):
    from src.mtool.scene import delete_scene

    scene = dummy_object.make_dummy_scene("generated_new_scene")

    new_scene = entry_scene.new_scene(scene, scene_root, history_db)
    assert new_scene[1] == "generated_new_scene"

    delete_scene.delete_scene("generated_new_scene", scene_root, history_db)


def test_history(setup, setup_telemetry, generate_short_history, scene_root, history_db, library_db, current_scene_db):
    assert len(entry_scene.history("", scene_root, history_db, library_db, current_scene_db)) == 1

