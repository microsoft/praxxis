from src.mtool.scene import resume_scene

def test_resume_scene(args, scene_root, history_db):
    resume_scene.resume_scene(args, scene_root, history_db)