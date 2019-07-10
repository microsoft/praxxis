import pytest 

@pytest.fixture(scope="function")
def setup_telemetry(telemetry_db):
    pass