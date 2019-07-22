class Dummy_Object():
    """
    a standin for the argparse namespace. Usable for every object. 
    """
    name = ""
    value = ""
    term = ""
    notebook = ""
    html = ""
    action = ""
    modelpath = ""
    converterpath = ""
    library_name = ""
    _hasParameters = ""
    dest = ""
    help = ""
    choices = ""
    option_strings = ""
    metavar=""
    _path = ""
    which = ""
    path = ""
    environment=""

    def getpath(self):
        """returns the path of the notebook"""
        return self._path

def make_dummy_object(name="", value="", term="", notebook="", html=""):
    dummy_object = Dummy_Object()
    dummy_object.name = name
    dummy_object.value = value
    dummy_object.term = term
    return dummy_object


def make_dummy_notebook(html="", path="", environment=""):
    import os

    dummy_notebook = Dummy_Object()
    dummy_notebook.notebook = "test_notebook"
    dummy_notebook.library_name = "test_notebooks"
    dummy_notebook.name = "test_notebook"
    dummy_notebook._path = os.path.join(path, "test_notebook.ipynb")
    dummy_notebook._hasParameters = False
    dummy_notebook.environment = environment
    dummy_notebook.html = html
    return dummy_notebook


def make_dummy_notebook_params(html = "", path=""):
    import os

    dummy_notebook = Dummy_Object()
    dummy_notebook.notebook = "test_param_inject"
    dummy_notebook.library_name = "test_notebooks"
    dummy_notebook._path = os.path.join(path, "test_param_inject.ipynb")
    dummy_notebook._hasParameters = True

    dummy_notebook.html = html
    return dummy_notebook


def make_dummy_notebook_envs():
    dummy_notebook_envs = Dummy_Object()

    dummy_notebook_envs.environment = [('text_to_print', '"hello world"'), ('times', '4')]
    return dummy_notebook_envs



def make_dummy_scene(name):
    dummy_scene = Dummy_Object()
    dummy_scene.name = name
    return dummy_scene


def make_dummy_search():
    dummy_search = Dummy_Object()
    dummy_search.term = "test"
    return dummy_search


def make_dummy_environment(name, value):
    dummy_environment = Dummy_Object()
    dummy_environment.name = name
    dummy_environment.value = value
    return dummy_environment


def make_dummy_action(dest, choices, help):
    dummy_action = Dummy_Object()
    dummy_action.dest = dest
    dummy_action.choices = choices
    dummy_action.help = help
    return dummy_action


def make_dummy_input(which):
    dummy_input = Dummy_Object()
    dummy_input.which = which
    dummy_input.notebook = "1"
    return dummy_input


def make_dummy_library():
    dummy_library = Dummy_Object()
    dummy_library.name = "test_notebooks"
    return dummy_library


def make_dummy_library_path():
    import os

    dummy_library_path = Dummy_Object()
    dummy_library_path.path = os.path.abspath(os.path.join('tests', 'test_notebooks'))
    dummy_library_path.name = "test_notebooks"
    return dummy_library_path


def make_dummy_notebook_path():
    import os

    dummy_notebook_path = Dummy_Object()
    dummy_notebook_path.path = os.path.abspath(os.path.join('tests', 'test_notebooks', 'test_notebook.ipynb'))
    return dummy_notebook_path

def make_dummy_ruleset(name):
    dummy_ruleset = Dummy_Object()
    dummy_ruleset.name = name
    return dummy_ruleset