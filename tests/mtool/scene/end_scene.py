from src.mtool.scene import end_scene

def test_end_scene(args, scene_root, history_db, current_scene_db):
    end_scene.end_scene(args, scene_root, history_db, current_scene_db)