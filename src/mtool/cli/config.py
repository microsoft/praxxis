import sys
import os
from collections import OrderedDict

def import_or_install(package):
    """One time install of package
    
    https://stackoverflow.com/questions/49839610/attributeerror-module-pip-has-no-attribute-main
    """
    try:
        return __import__(package)
    except ImportError:
        try:
            print("\nPIP INSTALL: Performing one time pip install: '" + package + "' package\n")
            import pip
            return pip.main(['install', package])
        except AttributeError:
            try:
                from pip._internal import main

                return main(['install', package])
            except Exception:
                print(f"REQUIRED: Unable to install package '{package}'.  Please perform a one manual install of {package}: 'pip3 install {package}'\n")

toml = import_or_install('toml')

def load(filename):
    """Load toml as dict"""
    if os.path.isfile(filename):
        dict = toml.load(filename)
    else:
        print(filename)
        dict = {}

    return dict

def load_ordered(filename):
    """Load toml as ordered dict"""
    if os.path.isfile(filename):
        dict = toml.load(filename, _dict=OrderedDict)
    else:
        dict = {}

    return dict

def save(filename, dict):
    """Save toml dictionary in file"""
    serial = toml.dumps(dict)

    with open(filename, 'w') as outfile:
        outfile.write(serial)

def delete(filename):
    """Delete a file"""
    os.remove(filename)