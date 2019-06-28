import pytest 
import sys 
import os

def test_init():
    """
    initializes testing. 
    In order to test mtool, a library of test notebooks needs to be in place.
    """ 

    if(sys.platform == "linux"):
        _root = os.path.join (os.path.expanduser('~/mtool'))
        _azure_data_studio_location = os.path.join('/usr', 'share', 'azuredatastudio', 'azuredatastudio')

    else:
        _root = os.path.join(os.getenv('APPDATA'), "mtool")
        _azure_data_studio_location = os.path.join(os.getenv('LOCALAPPDATA'), 'Programs', 'Azure Data Studio', 'azuredatastudio')
    
    _library_root = os.path.join(_root, "library")
    _library_db = os.path.join(_library_root, "libraries.db")
    _scene_root = os.path.join(_root, "scene")
    _outfile_root = os.path.join(_root, "output")
    _history_db = os.path.join(_scene_root, "current_scene.db")

    os.symlink("test_notebooks", _library_root, True)
