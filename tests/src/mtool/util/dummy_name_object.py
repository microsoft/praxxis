class Dummy_Object():
    """
    a standin for the argparse namespace. Usable for every object. 
    """
    name = ""
    value = ""
    term = ""

def make_dummy_object(name, value="", term=""):
    dummy_object = Dummy_Object()
    dummy_object.name = name
    dummy_object.value = value
    dummy_object.term = term
    return dummy_object