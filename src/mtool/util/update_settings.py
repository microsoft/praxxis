"""opens an interactive update utility in the console"""
from src.mtool.util.sqlite import sqlite_telemetry
from src.mtool.display import display_settings

def update_settings(user_info_db):
    SETTINGS = ["TELEMETRY", "URL", "Host", "Username", "Password"]
    settings_help = ["Set 0 to disable telemetry, 1 to enable", "WARNING-- do not alter if using SQL Server BDC \n\t(default: https://{0}:30443/gateway/default/webhdfs/v1/mtool)",
        "IP address of server", "Your username", "Your password"]

    values = sqlite_telemetry.get_settings(user_info_db, SETTINGS)
    
    display_settings.display_opening_message()

    display_settings.display_settings(SETTINGS, values)
    userIn = display_settings.display_menu_prompt()
    while userIn != '0':
        try:
            ordinal = int(userIn)
            if(ordinal in range(1, len(SETTINGS)+1)):
                setting = SETTINGS[ordinal-1]
                setting_help = settings_help[ordinal-1]
                values[setting] = display_settings.display_value_prompt(setting, setting_help)
                sqlite_telemetry.write_setting(user_info_db, setting, values[setting])
                display_settings.display_value_updated(setting, values[setting])
            else:
                raise ValueError
        except ValueError:
            from src.mtool.display import display_error
            display_error.settings_invalid_ordinal(userIn)

        display_settings.display_settings(SETTINGS, values)
        userIn = display_settings.display_menu_prompt()
            