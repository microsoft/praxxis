def init_telemetry(telemetry_db, 
                   send_telemetry = 1):
    from src.mtool.util.sqlite import sqlite_telemetry
    from src.mtool.display import display_error

    sqlite_telemetry.init_user_info(telemetry_db, send_telemetry)
    display_error.telem_not_init_warning()
