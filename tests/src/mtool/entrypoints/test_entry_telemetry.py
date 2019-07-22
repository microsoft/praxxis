from src.mtool.entrypoints import entry_telemetry

def test_init_telemetry(setup, telemetry_db):
    import os 

    if os.path.exists(telemetry_db):
        os.remove(telemetry_db)
    assert not os.path.exists(telemetry_db)
    
    entry_telemetry.init_telemetry(telemetry_db, 0)
