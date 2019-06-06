"""
"""



class Notebook:
    _hasParameters = False
    _environmentVars = []
    
    def __init__(self, path):

        print("hello world")

    # open notebook as json
    # extract parameters tag for first code block 
    # if parameters tag exists, extract environment variables from first code block source
