"""
This file contains the Scene class, with methods for managing the operations
that can be performed on mtool scenes.

Dependencies within mtool: helpers/config.py
"""

import sys
import os
import uuid
import glob
import datetime
import json

from src.mtool.cli import config

class Scene:
    """The mtool concept of a scene"""
    _root_folder = None
    _folder_name = "scene"
    _default_scene_name = 'scene-1'
    _id_file = "id.json"
    _id_current_scene = None

    def __init__(self, root_folder):
        """Creates a scene in the root folder, making folder for it"""
        self._root_folder = os.path.join(root_folder, self._folder_name)
        self._id_current_scene = os.path.join(self._root_folder, "current_scene.json")

        if not os.path.exists(self._root_folder):
            os.mkdir(self._root_folder)

        if not self.are_there_any_scenes():
            self.create(self._default_scene_name)

    def are_there_any_scenes(self):
        """Determines whether any scenes currently exist"""
        are_there_scenes = False
        for root, dirs, files in os.walk(os.path.join(self._root_folder)):
            for name in dirs:
                are_there_scenes = True
                break

        return are_there_scenes

    @property
    def get_current_scene_directory(self):
        """Returns current scene's directory"""
        return os.path.join(self._root_folder, self.current)

    def get_scene_directory(self, name):
        """Returns directory of the scene <name>"""
        return os.path.join(self._root_folder, name)

    @property
    def current(self):
        """Returns current scene information"""
        with open(self._id_current_scene, 'r') as file:
            return file.read()

    @property
    def scenes_json_filename(self):
        """Returns path to json file for scene"""
        return os.path.join(self._root_folder, "scenes.json")

    def create(self, nameHint):
        """Creates a new scene, handling repeat names"""
        nameHint = nameHint.lower()
        nameHint = nameHint.replace(' ', '-')

        directory = self.get_scene_directory(nameHint)

        postfix = 0
        name = nameHint
        nameHint = nameHint + "-"
        while os.path.exists(directory):
            postfix += 1
            name = nameHint + str(postfix)
            directory = self.get_scene_directory(name)

        os.mkdir(directory)

        with open(os.path.join(directory, self._id_file), 'w') as outfile:
            outfile.write(str(uuid.uuid4()))

        self.set(name)

        return name

    def delete(self, name):
        """Deletes a scene and all related information"""
        directory = self.get_scene_directory(name)

        if os.path.exists(directory):
            files = glob.glob(os.path.join(directory, "*"))
            for f in files:
                os.remove(f)

            os.rmdir(directory)

            # If we just deleted the current scene, select another one if there is
            # one.
            if self.current == name:
                for root, dirs, files in os.walk(os.path.join(self._root_folder)):
                    for n in dirs:
                        self.set(n)
                        return n

            # if there isn't a scene left, a new 'scene-1' will be created next time
            if self.current == name:
                name = self._default_scene_name
        else:
            raise Exception("Unable to delete scene '{0}', '{1}' not found". format(name, directory))

        return name

    def end(self):
        """End the current scene"""
        name = self.current
        directory = self.get_scene_directory(name)

        end_scene_file = os.path.join(directory, "end-scene.json")

        if not os.path.isfile(end_scene_file):
            with open(end_scene_file, 'w') as outfile:
                outfile.write(str(datetime.datetime.now()))

        return name

    def is_scene_active(self):
        """Returns whether the scene is currently active"""
        name = self.current
        directory = self.get_scene_directory(name)

        end_scene_file = os.path.join(directory, "end-scene.json")

        if os.path.isfile(end_scene_file):
            return False
        else:
            return True
 
    def resume(self):
        """Resumes a scene"""
        name = self.current
        directory = self.get_scene_directory(name)

        end_scene_file = os.path.join(directory, "end-scene.json")

        if os.path.isfile(end_scene_file):
            os.remove(end_scene_file)

        return name

    def set(self, name):
        """Sets name for the current scene"""
        directory = self.get_scene_directory(name)

        # Might as well create it if it doesn't exist
        if not os.path.exists(directory):
            self.create(name)

        with open(self._id_current_scene, 'w') as outfile:
            outfile.write(name)

        return name

    def list(self):
        """List all scenes by time of creation"""
        items = []

        # Get scenes by date they were created
        os.chdir(self._root_folder)
        files = sorted(os.listdir('.'), key=os.path.getctime)
        dirs = list(filter(lambda x: os.path.isdir(x), files))
        counter = len(dirs)

        def print_scene(counter, name):
            """Prints a scene to console"""
            print ("\t{0}. {1}".format(str(counter), name))
            items.append([counter, name])

        def is_scene_ended(name):
            """Determines whether a scene has been ended"""
            return not os.path.isfile(os.path.join(self._root_folder, name, "end-scene.json"))

        def print_scenes(display_text, dirs, counter, ended_scenes):
            """Prints a set of scenes, ended and active both"""
            print()
            print (f"{display_text}:")
            print ()
            for name in dirs:
                if ended_scenes:
                    if is_scene_ended(name):
                        continue
                else:
                    if not is_scene_ended(name):
                        continue

                print_scene(counter, name)
                counter -= 1

            return counter

        counter = print_scenes("Ended scenes", dirs, counter, True)
        
        print_scenes("Active scenes", dirs, counter, False)

        with open(self.scenes_json_filename, 'w') as outfile:
            outfile.write(json.dumps(items))

    def set_environment_overrides(self):
        """Set up environment overrides for current scene"""
        toml_filename = os.path.join(self.get_current_scene_directory, "custom.toml")

        os.environ["MTOOL_CURRENT_SCENE"] =  self.current

        if os.path.isfile(toml_filename):
            dict = config.load(toml_filename)

            print()
            print('Environment overrides for current scene:')
            for key, value in dict.items():
                os.environ[key] = value
                print(f'\t{key}={value}')

