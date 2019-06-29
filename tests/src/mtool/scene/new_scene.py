from src.mtool.scene import new_scene

def test_new_scene(args, scene_root, history_db):
    new_scene.new_scene(args, scene_root, history_db)