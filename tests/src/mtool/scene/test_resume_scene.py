def test_resume_scene(setup, scene_root, history_db):
    from src.mtool.scene import resume_scene
    from tests.src.mtool.util import dummy_name_object
    from src.mtool.util.sqlite import sqlite_scene

    # notebook1 = dummy_name_object.make_dummy_scene("generated_ended_scene")
    # resume_scene.resume_scene(notebook1, scene_root, history_db)
    # ended_scenes = sqlite_scene.get_ended_scenes(history_db)
    # print(ended_scenes)

    # assert "generated_ended_scene" in sqlite_scene.get_ended_scenes(history_db)

