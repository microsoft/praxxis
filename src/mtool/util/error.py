class NotebookNotFoundError(Exception):
    def __init__(self, name=None):
        self.name = name


    def __str__(self):
        from src.mtool.display import display_error
        return repr(display_error.notebook_not_found_error(self.name))


class EnvNotFoundError(Exception):
    def __init__(self, name=None):
        self.name = name
    

    def __str__(self):
        from src.mtool.display import display_error
        return str(display_error.env_not_found_error(self.name))