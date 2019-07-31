def test_backlog_creation_file_update(setup, telemetry_db, add_test_library):
    """tests whether backlog is initialized when updating a file"""
    from src.praxxis.telemetry import update_file_output
    from src.praxxis.sqlite import sqlite_telemetry
    from tests.src.praxxis.util import dummy_object
    
    notebook1 = dummy_object.make_dummy_notebook()
    ID = "garbageID"
    update_file_output.update_file(telemetry_db, notebook1.path, ID)

    backlog = sqlite_telemetry.get_backlog(telemetry_db)
    backlog_len = sqlite_telemetry.backlog_size(telemetry_db)

    assert len(backlog) == 1
    assert len(backlog) == backlog_len

    # check format of backlog
    assert len(backlog[0]) == 3
    assert backlog[0][0] == notebook1.path
    assert backlog[0][1] == ID
    assert backlog[0][2] == 1 # failed on delete
    
    sqlite_telemetry.clear_backlog(telemetry_db)

