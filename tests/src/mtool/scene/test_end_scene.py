import pytest
@pytest.mark.skip(reason="init scene things are broken")
def test_end_scene_success(setup, setup_sqlite, create_many_scenes, default_scene_name, scene_root, history_db, current_scene_db):
    import argparse
    from src.mtool.scene import end_scene
    from src.mtool.scene import list_scene

    namespace = argparse.Namespace
    namespace.name = default_scene_name
    scene_list = list_scene.list_scene(namespace, history_db)[0]
    
    before_end = len(scene_list)
    end_scene.end_scene(namespace, scene_root, history_db, current_scene_db)
    after_end = list_scene.list_scene(namespace, history_db)[0]
    
    # assert before_end + 1 == len(after_end)

@pytest.mark.skip(reason="init scene things are broken")
def test_end_scene_last_scene(setup, setup_sqlite, default_scene_name, scene_root, history_db, current_scene_db):    
    import argparse
    from src.mtool.scene import end_scene
    from src.mtool.scene import list_scene

    namespace = argparse.Namespace
    namespace.name = default_scene_name
    scene_list = list_scene.list_scene(namespace, history_db)[0]
    
    before_end = len(scene_list)
    end_scene.end_scene(namespace, scene_root, history_db, current_scene_db)
    after_end = list_scene.list_scene(namespace, history_db)[0]
    
    assert before_end  == len(after_end)