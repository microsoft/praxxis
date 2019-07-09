import pytest 

@pytest.fixture(scope="function")
def setup_telemetry(telemetry_db):
    from src.mtool.util.sqlite import sqlite_telemetry
    import os

    sqlite_telemetry.init_user_info(telemetry_db, 0)
    yield
    os.remove(telemetry_db)
    assert not os.path.exists(telemetry_db)
