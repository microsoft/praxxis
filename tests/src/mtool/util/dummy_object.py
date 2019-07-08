class Dummy_Object():
    """
    a standin for the argparse namespace. Usable for every object. 
    """
    name = ""
    value = ""
    term = ""
    notebook = ""
    html = ""
    library_name = ""
    _hasParameters = ""
    dest = ""
    help = ""
    choices = ""
    option_strings = ""
    metavar=""


def make_dummy_object(name="", value="", term="", notebook="", html=""):
    dummy_object = Dummy_Object()
    dummy_object.name = name
    dummy_object.value = value
    dummy_object.term = term
    return dummy_object


def make_dummy_notebook(html=""):
    dummy_notebook = Dummy_Object()
    dummy_notebook.notebook = "DIR001 - dir"
    dummy_notebook.library_name = "test_notebooks"
    dummy_notebook._hasParameters = False

    dummy_notebook.html = html
    return dummy_notebook


def make_dummy_scene(name):
    dummy_scene = Dummy_Object()
    dummy_scene.name = name
    return dummy_scene


def make_dummy_search():
    dummy_search = Dummy_Object()
    dummy_search.term = "DIR"
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
