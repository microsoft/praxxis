from src.mtool.scene import scene

def test_init_scene(scene_root, history_db):
    scene.init_scene(scene_root, history_db)


def test_get_scene_by_ordinal(args, name, history_db):
    scene.get_scene_by_ordinal(args, name, history_db)