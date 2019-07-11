class NotebookNotFoundError(Exception):
    def __init__(self, name=None):
        self.name = name


    def __str__(self):
        from src.mtool.display import display_error
        return str(display_error.notebook_not_found_error(self.name))


class EnvNotFoundError(Exception):
    def __init__(self, name=None):
        self.name = name
    

    def __str__(self):
        from src.mtool.display import display_error
        return str(display_error.env_not_found_error(self.name))


class SceneNotFoundError(Exception):
    def __init__(self, name=None):
        self.name = name
    

    def __str__(self):
        from src.mtool.display import display_error
        return str(display_error.scene_not_found_error(self.name))


class SceneEndedError(Exception):
    def __init__(self, name=None):
        self.name = name
    

    def __str__(self):
        from src.mtool.display import display_error
        return str(display_error.scene_ended_error(self.name))


class LastActiveSceneError(Exception):    
    def __init__(self, name=None):
        self.name = name
    

    def __str__(self):
        from src.mtool.display import display_error
        return str(display_error.last_active_scene_error(self.name))


class EndEndedSceneError(Exception):
    def __init__(self, name=None):
        self.name = name
    
    def __str__(self):
        from src.mtool.display import display_error
        return str(display_error.end_ended_scene_error(self.name))


class LibraryNotFoundError(Exception):
    def __init__(self, name=None):
        self.name = name
    
    def __str__(self):
        from src.mtool.display import display_error
        return str(display_error.library_not_found_error(self.name))


class NotDirectoryError(Exception):
    def __init__(self, name=None):
        self.name = name
    
    def __str__(self):
        from src.mtool.display import display_error
        return str(display_error.not_directory_error(self.name))