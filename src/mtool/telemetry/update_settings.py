"""opens an interactive update utility in the console"""
from src.mtool.sqlite import sqlite_telemetry
from src.mtool.display import display_settings

_settings = ["TELEMETRY", "URL", "Host", "Username", "Password"]
_settings_help = ["Set 0 to disable telemetry, 1 to enable", "WARNING-- do not alter if using SQL Server BDC \n\t(default: https://{0}:30443/gateway/default/webhdfs/v1/mtool)",
        "IP address of server", "Your username", "Your password"]

def update_settings(user_info_db):
    values = get_values(user_info_db)
    
    display_settings.display_opening_message()

    display_settings.display_settings(_settings, values)
    user_in = display_settings.display_menu_prompt()
    while user_in != 'q':
        get_ordinal(user_in, values, user_info_db)

        display_settings.display_settings(_settings, values)
        user_in = display_settings.display_menu_prompt()
    return 0


def get_values(user_info_db):
    return sqlite_telemetry.get_settings(user_info_db, _settings)


def get_ordinal(user_in, values, user_info_db):
        try:
            ordinal = int(user_in)
            if(ordinal in range(1, len(_settings)+1)):
                edit_settings(ordinal, values, user_info_db)
            else:
                raise ValueError
        except ValueError:
            from src.mtool.display import display_error
            display_error.settings_invalid_ordinal(user_in)
            return "not_ordinal"


def edit_settings(ordinal, values, user_info_db):
    setting = _settings[ordinal-1]
    setting_help = _settings_help[ordinal-1]
    values[setting] = display_settings.display_value_prompt(setting, setting_help)
    sqlite_telemetry.write_setting(user_info_db, setting, values[setting])
    display_settings.display_value_updated(setting, values[setting])
