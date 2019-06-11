"""
This file contains the functions that the other files call to implement mtool.

Dependencies within mtool: spinner.py, scene.py, environment.py, telemetry.py, log.py
    helpers/args.py, helpers/file_io.py
"""

import os
import sys
import time
import uuid
import papermill 

import traceback

from src.mtool.util import spinner
from src.mtool.scene import scene
from src.mtool.environment import environment
from src.mtool.cli import telemetry
from src.mtool.util import log
from src.mtool.cli import args
from src.mtool.cli import file_io
from src.mtool.notebook.notebook import Notebook

class Mtool:
    """Methods for the operation of the tool"""
    # Libraries can exist in current dir (shared), or in user's local working dir (personal)
    _library_roots = ["%APPDATA%\\mtool\\library"] 
    _loc = __file__

    spinner = spinner.Spinner() # Spinning progress animation for the console
    
    _working_folder_name = "mtool"
    _id_file = "id.json"

    _scene = None
    _environment = None

    _log = None
    _args = None

    def __init__(self, argv):
        """Starts up mtool with scene, environment, and args"""
        sys.excepthook = self._capture_unhandled_exception

        self._library_roots.append(os.path.join(self._loc, "..\\library"))
        ##TODO: APPDATA is Windows specific!
        directory = os.path.join(os.getenv('APPDATA'), self._working_folder_name)

        self._write_installation_identifier(directory)
        self._scene = scene.Scene(directory)
        self._environment = environment.Environment(self._library_roots, self.working_dir)
        self._args = args.Args(argv)

        print('Current Scene: {0}'.format(self.current_scene))


    @property
    def show_notebook_in_web_browser(self):
        """Returns html of notebook"""
        return self.args.to_html

    @property
    def args(self):
        """Returns current set of arguments"""
        return self._args

    @property
    def log(self):
        """Creates log, if not present"""
        if self._log is None:
            self._log = log.Log()

        return self._log

    @property
    def list_filename(self):
        """Returns the filename of the list"""
        return os.path.join(self.working_dir, 'list.json')

    @property
    def list_exist(self):
        """Returns whether a list exists"""
        return os.path.isfile(self.list_filename)

    @property
    def get_list(self):
        """Returns list of items"""
        return file_io.load_json(self.list_filename)

    def write_list(self, items):
        """Writes list of items to file"""
        file_io.save_json(self.list_filename, items)

    def _write_installation_identifier(self, directory):
        """Writes unique installation identifier to directory"""
        self._id_file = os.path.join(directory, "id.json")

        if not os.path.isfile(self._id_file):
            if not os.path.exists(directory):
                os.mkdir(directory)

            with open(self._id_file, 'w') as outfile:
                outfile.write(str(uuid.uuid4()))

    def for_each_notebook(self, root, fn):
        """Calls fn for each notebook in directory tree at root"""
        Notebook.for_each_notebook(root, fn)

    def for_each_notebook_specified_on_command_line(self, fn):
        """Calls fn for each notebook listed on command line"""
        if not self._scene.is_scene_active():
            raise Exception('Scene is not active, please resume scene (m rs) or create a new one (m cs)')
        nb = Notebook(os.path.join(self.args.ordinal_to_list_item(self.list_filename)))
        local_copy = nb.execute()
        self.send_telemetry(local_copy)

    def for_each_notebook_in_scene_history(self, uniquify, fn):
        """Calls fn for each unique (if uniquify) notebook in scene history"""
        previous = ""

        for root, dirs, files in os.walk(os.path.join(self.working_dir)):
            for file in files:
                parts = os.path.splitext(file)

                if(parts[1] == '.ipynb'):
                    filename_without_extension = parts[0]

                    # Remove the first 'n' chars, and then remove the library name
                    remove_timestamp_in_filename=filename_without_extension[filename_without_extension.find('-', 12) + 1:]
                    library_name=remove_timestamp_in_filename[0:remove_timestamp_in_filename.find('-')]
                    name=remove_timestamp_in_filename[remove_timestamp_in_filename.find('-') + 1:]

                    if (not uniquify or (remove_timestamp_in_filename != previous)):
                        fn(name, library_name)
                    
                    previous = name

    @property
    def working_dir(self):
        """Get the working directory for current scene"""
        return self._scene.get_current_scene_directory

    def create_scene(self):
        """Create a new scene"""
        return self._scene.create(self.args.first_arg_lower)

    def delete_scene(self):
        """Delete a scene, current one if no argument provided"""
        if self.args.arg_provided:
            scene_name = self.args.ordinal_to_list_item(self._scene.scenes_json_filename)
        else:
            scene_name = self._scene.current
        return self._scene.delete(scene_name)

    def list_scenes(self):
        """List all scenes"""
        self._scene.list()

    def set_scene(self):
        """Set the current scene"""
        return self._scene.set(self.args.ordinal_to_list_item(self._scene.scenes_json_filename))

    def end_scene(self):
        """End a scene"""
        return self._scene.end()

    def resume_scene(self):
        """Resume previously ended scene"""
        return self._scene.resume()

    @property
    def current_scene(self):
        """Returns the current scene"""
        return self._scene.current

    def list_env(self):
        """Lists environment variables"""
        return self._environment.list()

    def set_env(self):
        """Sets an environment variable"""
        return self._environment.set(self.args.ordinal_to_list_item(self._environment.list_json_filename), self.args.the_value)

    def delete_env(self):
        """Deletes an environment variable"""
        return self._environment.delete(self.args.ordinal_to_list_item(self._environment.list_json_filename))

    def set_environment_overrides_for_scene(self):
        """Sets any overrides of the toml file"""
        self._scene.set_environment_overrides()

    def for_each_library(self, fn):
        """Calls fn for each library"""
        for root in self._library_roots:
            if os.path.isdir(root):
                for library_name in os.listdir(os.path.expandvars(root)):
                    fn(root, library_name)

    def send_telemetry(self, local_copy):
        """Sends telemetry to HDFS"""
        with open(self._id_file) as infile:
            id = infile.read()

        with open(os.path.join(self.working_dir, "id.json")) as infile:
            scene_id = infile.read()

        telemetry.send(id, scene_id, local_copy)

    def _capture_unhandled_exception(self, exctype, value, tb):
        """Highest level of exception handling"""
        if Mtool.spinner is not None:
            Mtool.spinner.stop()

        print('\n\nmtool hit an unhandled exception:\n')
        traceback.print_exception(exctype, value, tb, file=sys.stdout)
    