def test_change_scene(setup, setup_sqlite, create_many_scenes, scene_root, history_db, default_scene_name):
    import argparse
    from src.mtool.scene import change_scene

    namespace = argparse.Namespace
    namespace.name = f"{default_scene_name}-1"
    
    change_scene.change_scene(namespace, scene_root, history_db)