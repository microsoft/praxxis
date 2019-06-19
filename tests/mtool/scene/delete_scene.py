from src.mtool.scene import delete_scene

def test_delete_scene(args, root, history_db):
    delete_scene.delete_scene(args, root, history_db)