
def test_backlog_creation(setup, telemetry_db, add_test_library):
    """tests whether backlog is initialized"""
    from src.praxxis.telemetry import telemetry
    from src.praxxis.sqlite import sqlite_telemetry
    from tests.src.praxxis.util import dummy_object
    
    notebook1 = dummy_object.make_dummy_notebook()
    ID = "garbageID"
    telemetry.telem_entrance(telemetry_db, notebook1.path, ID)

    backlog = sqlite_telemetry.get_backlog(telemetry_db)

    assert len(backlog) == 1

def test_backlog_continuation(setup, telemetry_db, add_test_library):
    """tests that backlog continues to be updated"""
    from src.praxxis.telemetry import telemetry
    from src.praxxis.sqlite import sqlite_telemetry
    from tests.src.praxxis.util import dummy_object

    sqlite_telemetry.clear_backlog(telemetry_db)
    
    notebook1 = dummy_object.make_dummy_notebook()
    notebook2 = dummy_object.make_dummy_notebook()
    ID = "garbageID"
    telemetry.telem_entrance(telemetry_db, "notebook1.path", ID)
    telemetry.telem_entrance(telemetry_db, "notebook2.path", ID)

    backlog = sqlite_telemetry.get_backlog(telemetry_db)

    assert len(backlog) == 2