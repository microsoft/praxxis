"""
This file DOES A THING

Dependencies within mtool: helpers/file_io
"""

import os
import sys

# Include the helpers subfolder folder
#
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), "helpers"))

import config
import file_io

class Environment:

    _root_folders = None
    _toml_filename = None # The user's per scene environment variable overrides
    _list_filename = None # The list of envionment variables and their ordinals, 1, 2, 3 etc.

    def __init__(self, library_root_folders, working_dir):
        self._root_folders = library_root_folders
        self._toml_filename = os.path.join(working_dir, "custom.toml")
        self._list_filename = os.path.join(working_dir, "environment-list.json")

    @property
    def list_json_filename(self):
        return self._list_filename

    def list(self):
        dict = config.load(self._toml_filename)
        items = self.get_variables_for_all_libraries(dict)
        file_io.save_json(self._list_filename, items)

    def set(self, name, value):

        name = name.upper() # Follow norm of environment variabels in CAPS

        if os.path.isfile(self._toml_filename):
            dict = config.load(self._toml_filename)
            dict[name] = value
        else:
            dict = { name: value }

        config.save(self._toml_filename, dict)

    def delete(self, name):

        name = name.upper() # Follow norm of environment variabels in CAPS

        if os.path.isfile(self._toml_filename):
            dict = config.load(self._toml_filename)

            if name in dict:
                del dict[name]

                if len(dict) == 0:
                    config.delete(self._toml_filename)
                else:
                    config.save(self._toml_filename, dict)

    def get_variables_for_all_libraries(self, overrides):

        items = []
        count = 0
        for library_root in self._root_folders:
            root =  os.path.expandvars(library_root)

            if os.path.isdir(root):
                for library in os.listdir(root):
                    toml_filename = os.path.join(root, library, 'environment.toml')

                    if os.path.isfile(toml_filename):
                        dict = config.load_ordered(toml_filename)
                        prefix = dict['prefix']

                        for name, section in dict.items():
                            if type(section) == type(dict):
                                section_name = name

                                for key, value in section.items():
                                    variable = section_name + "_" + key
                                    env_variable = prefix.upper() + "_" + variable.upper()

                                    if env_variable in overrides:
                                        value = overrides[env_variable]
                                        override_marker = "* "
                                    else:
                                        override_marker = ""

                                    count += 1
                                    print("\t{0}. {1}{2} = {3}".format(count, override_marker, env_variable, value))
                                    items.append([count, env_variable])

        return items