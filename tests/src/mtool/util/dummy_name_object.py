class Dummy_Object():
    """
    a standin for the argparse namespace. Usable for every object. 
    """
    name = ""
    value = ""
    term = ""
    notebook = ""
    html = ""

def make_dummy_object(name="", value="", term="", notebook="", html=""):
    dummy_object = Dummy_Object()
    dummy_object.name = name
    dummy_object.value = value
    dummy_object.term = term
    return dummy_object

def make_dummy_notebook(notebook, html=""):
    dummy_notebook = Dummy_Object()
    dummy_notebook.notebook = notebook
    dummy_notebook.html = html
    return dummy_notebook

def make_dummy_scene(name):
    dummy_scene = Dummy_Object()
    dummy_scene.name = name
    return dummy_scene