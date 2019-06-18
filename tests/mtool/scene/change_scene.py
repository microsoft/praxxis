from src.mtool.scene import change_scene

def test_change_scene(args, scene_root, history_db):
    change_scene.change_scene(args, scene_root, history_db)