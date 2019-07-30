from src.praxxis.util import roots

def test_init(setup, init_root, library_root, library_db, outfile_root, scene_root, history_db, telemetry_db, rulesengine_root, rulesengine_db, model_root, model_db, default_scene_name):
    pass
    from src.praxxis.util import rmtree
    import os 
    
    assert os.path.exists(init_root)
    rmtree.rmtree(init_root, test=True)
    assert not os.path.exists(init_root)
    roots.init(init_root, library_root, library_db, outfile_root, scene_root, history_db, telemetry_db, rulesengine_root, rulesengine_db, model_root, model_db, default_scene_name, False)
    
    assert os.path.exists(init_root)
    assert os.path.exists(library_root)
    assert os.path.exists(library_db)
    assert os.path.exists(outfile_root)
    assert os.path.exists(scene_root)
    assert os.path.exists(history_db)
    assert os.path.exists(telemetry_db)

def test_get_current_scene_db(setup, scene_root, history_db):
    import os
    
    current_scene_db = roots.get_current_scene_db(scene_root, history_db)
    assert os.path.basename(current_scene_db) == "scene.db"
