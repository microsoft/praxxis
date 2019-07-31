def test_backlog_creation_file_update(setup, telemetry_db, add_test_library):
    """tests whether backlog is initialized when updating a file"""
    from src.praxxis.telemetry import update_file_output
    from src.praxxis.sqlite import sqlite_telemetry
    from tests.src.praxxis.util import dummy_object
    
    notebook1 = dummy_object.make_dummy_notebook()
    ID = "garbageID"
    
    # turn on telem setting
    sqlite_telemetry.write_setting(telemetry_db, "TELEMETRY", 1)
    assert sqlite_telemetry.telem_on(telemetry_db)

    update_file_output.update_file_output_entrance(telemetry_db, notebook1.path, ID)

    backlog = sqlite_telemetry.get_backlog(telemetry_db)
    backlog_len = sqlite_telemetry.backlog_size(telemetry_db)

    assert len(backlog) == 1
    assert len(backlog) == backlog_len

    # check format of backlog
    assert len(backlog[0]) == 3
    assert backlog[0][0] == notebook1.path
    assert backlog[0][1] == ID
    assert backlog[0][2] == 1 # failed on delete
    
    # cleanup
    sqlite_telemetry.clear_backlog(telemetry_db)
    sqlite_telemetry.write_setting(telemetry_db, "TELEMETRY", 0)

def test_telemetry_off(setup, telemetry_db, add_test_library):
    from src.praxxis.sqlite import sqlite_telemetry
    from src.praxxis.telemetry import update_file_output
    from src.praxxis.sqlite import sqlite_telemetry
    from tests.src.praxxis.util import dummy_object

    sqlite_telemetry.write_setting(telemetry_db, "TELEMETRY", 0)

    notebook1 = dummy_object.make_dummy_notebook()
    ID = "garbageID"
    update_file_output.update_file_output_entrance(telemetry_db, notebook1.path, ID)

    backlog_len = sqlite_telemetry.backlog_size(telemetry_db)

    assert backlog_len == 0
