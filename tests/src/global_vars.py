import os
import sys

global ROOT
global AZURE_DATA_STUDIO_LOCATION 
global LIBRARY_ROOT
global LIBRARY_DB 
global SCENE_ROOT 
global OUTFILE_ROOT
global HISTORY_DB 
global TELEMETRY_DB 
global DEFAULT_SCENE_NAME 


if(sys.platform == "linux"):
    ROOT = os.path.join(os.path.expanduser('~/mtool'), 'test')
    AZURE_DATA_STUDIO_LOCATION = os.path.join('/usr', 'share', 'azuredatastudio', 'azuredatastudio')

else:
    ROOT = os.path.join(os.getenv('APPDATA'), "mtool", 'test')
    AZURE_DATA_STUDIO_LOCATION = os.path.join(os.getenv('LOCALAPPDATA'), 'Programs', 'Azure Data Studio', 'azuredatastudio')

LIBRARY_ROOT = os.path.join(ROOT, "test_library")
LIBRARY_DB = os.path.join(LIBRARY_ROOT, "libraries.db")
SCENE_ROOT = os.path.join(ROOT, "test_scene")
OUTFILE_ROOT = os.path.join(ROOT, "test_output")
HISTORY_DB = os.path.join(SCENE_ROOT, "current_scene.db")
TELEMETRY_DB = os.path.join(ROOT, "user_id.db")
DEFAULT_SCENE_NAME = 'scene'