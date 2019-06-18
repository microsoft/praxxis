from src.mtool.scene import current_scene

def test_current_scene(scene_root, history_db):
    current_scene.current_scene(scene_root, history_db)