def test_resume_scene(setup, create_ended_scene, scene_root, history_db, current_scene_db):
    from src.mtool.scene import resume_scene
    from src.mtool.sqlite import sqlite_scene
    
    ended_scenes = sqlite_scene.get_ended_scenes(history_db)
    assert len(ended_scenes) == 1
    resume_scene.resume_scene("generated_ended_scene", scene_root, history_db)
    ended_scenes = sqlite_scene.get_ended_scenes(history_db)
    assert len(ended_scenes) == 0
