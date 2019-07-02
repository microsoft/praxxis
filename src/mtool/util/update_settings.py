"""opens an interactive update utility in the console"""
from src.mtool.util.sqlite import sqlite_telemetry
from src.mtool.display import display_settings

def update_settings(user_info_db):
    SETTINGS = ["TELEMETRY", "URL", "Host", "Username", "Password"]
    descriptions = ["Set 0 to disable telemetry, 1 to enable", "WARNING: do not alter if using SQL Server BDC",
        "IP address of server", "Your username", "Your password"]

    telem_values = sqlite_telemetry.get_telemetry_info(user_info_db)
    telem_values[3] = "*******" #don't pass display anything sensitive
    # (password doesn't print anyway but in case we change that)

    display_settings.display_opening_message()

    done = False
    while not done:
        display_settings.display_settings(SETTINGS, telem_values)
        userIn = display_settings.display_menu_prompt()

        if (userIn == '0' or userIn == 'exit'):
            done = True
        else:
            try:
                ordinal = int(userIn)
                if(ordinal in range(1, len(SETTINGS)+1)):
                    change_setting(SETTINGS[int(userIn) - 1], user_info_db)
                    telem_values = sqlite_telemetry.get_telemetry_info(user_info_db)
                else:
                    raise ValueError
            except ValueError:
                print("no")
            



def change_setting(setting, user_info_db):
    changeVal = display_settings.display_value_prompt(setting)
    sqlite_telemetry.write_setting(user_info_db, setting, changeVal)
    display_settings.display_value_updated(setting, changeVal)
    
