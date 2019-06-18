from src.mtool.scene import list_scene

def test_list_scene(root, history_db):
    list_scene.list_scene(root, history_db)