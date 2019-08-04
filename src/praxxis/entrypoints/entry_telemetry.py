"""
This file handles sending telemetry from the CLI
"""

from src.praxxis.util.roots import _telemetry_db
from src.praxxis.util.roots import _user_info_db

def init_telemetry(telemetry_db = _telemetry_db, 
                   send_telemetry = 1):
    """handles initializing the telemetry db and directory"""
    from src.praxxis.sqlite import sqlite_init
    from src.praxxis.display import display_error

    sqlite_init.init_user_info(telemetry_db, send_telemetry)
    display_error.telem_not_init_warning()


def update_settings(arg,
                    user_info_db = _user_info_db):
    """handles opening the settings utility"""
    from src.praxxis.telemetry import update_settings
    update_settings.update_settings(user_info_db)
