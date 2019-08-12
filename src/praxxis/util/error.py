"""
This file contains custom error definitions for praxxis operations.
"""

class NotebookNotFoundError(Exception):
    """thrown when a notebook can't be found for an op"""
    def __init__(self, name=None):
        self.name = name

    def __str__(self):
        from src.praxxis.display import display_error
        return str(display_error.notebook_not_found_error(self.name))


class RuleNotFoundError(Exception):
    """thrown when a rule can't be found for an op"""
    def __init__(self, name=None):
        self.name = name

    def __str__(self):
        from src.praxxis.display import display_error
        return str(display_error.rule_not_found_error(self.name))


class RulesetNotFoundError(Exception):
    """thrown when a ruleset can't be found for an op"""
    def __init__(self, name=None):
        self.name = name

    def __str__(self):
        from src.praxxis.display import display_error
        return str(display_error.ruleset_not_found_error(self.name))


class RulesetActiveError(Exception):
    """thrown when user attempts to active an active ruleset"""
    def __init__(self, name=None):
        self.name = name

    def __str__(self):
        from src.praxxis.display import display_error
        return str(display_error.ruleset_active_error(self.name))


class RulesetNotActiveError(Exception):
    """thrown when user attempts to deactivate a deactive ruleset"""
    def __init__(self, name=None):
        self.name = name

    def __str__(self):
        from src.praxxis.display import display_error
        return str(display_error.ruleset_not_active_error(self.name))


class ParamNotFoundError(Exception):
    """thrown when a param can't be found for an op"""
    def __init__(self, name=None):
        self.name = name    

    def __str__(self):
        from src.praxxis.display import display_error
        return str(display_error.param_not_found_error(self.name))


class SceneNotFoundError(Exception):
    """thrown when a scene can't be found for an op"""
    def __init__(self, name=None):
        self.name = name
    
    def __str__(self):
        from src.praxxis.display import display_error
        return str(display_error.scene_not_found_error(self.name))


class SceneEndedError(Exception):
    """thrown when user attempts to change to an ended scene"""
    def __init__(self, name=None):
        self.name = name
    
    def __str__(self):
        from src.praxxis.display import display_error
        return str(display_error.scene_ended_error(self.name))


class LastActiveSceneError(Exception):   
    """thrown when user attempts to end the last active scene"""
    def __init__(self, name=None):
        self.name = name
    
    def __str__(self):
        from src.praxxis.display import display_error
        return str(display_error.last_active_scene_error(self.name))


class EndEndedSceneError(Exception):
    """thrown when user attempts to end an ended scene"""
    def __init__(self, name=None):
        self.name = name
    
    def __str__(self):
        from src.praxxis.display import display_error
        return str(display_error.end_ended_scene_error(self.name))


class LibraryNotFoundError(Exception):
    """thrown when a library can't be found for an op"""
    def __init__(self, name=None):
        self.name = name
    
    def __str__(self):
        from src.praxxis.display import display_error
        return str(display_error.library_not_found_error(self.name))


class NotDirectoryError(Exception):
    """thrown when an op expects a directory path and is passed a file path"""
    def __init__(self, name=None):
        self.name = name
    
    def __str__(self):
        from src.praxxis.display import display_error
        return str(display_error.not_directory_error(self.name))

    
class NotFileError(Exception):
    """thrown when an op expects a file path and is passed a directory path"""
    def __init__(self, name=None):
        self.name = name
    
    def __str__(self):
        from src.praxxis.display import display_error
        return str(display_error.not_file_error(self.name))


class NotNotebookError(Exception):
    """thrown when user tries to add a non-.ipynb file with add notebook"""
    def __init__(self, name=None):
        self.name = name
    
    def __str__(self):
        from src.praxxis.display import display_error
        return str(display_error.not_notebook_error(self.name))


class DuplicateNotebookError(Exception):
    """thrown when two notebooks with the same name lack distinguishing info"""
    def __init__(self, name=None):
        self.name = name
    
    def __str__(self):
        from src.praxxis.display import display_error
        return str(display_error.duplicate_notebook_error(self.name))


class EditorNotFoundError(Exception):
    """thrown when the editor to open in doesn't exist"""
    def __init__(self, name=None):
        self.name = name
    
    def __str__(self):
        from src.praxxis.display import display_error
        return str(display_error.editor_not_found_error(self.name))


class ADSNotFoundError(Exception):
    """thrown when ADS is not in the expected place"""
    def __init__(self, name=None):
        self.name = name
    
    def __str__(self):
        from src.praxxis.display import display_error
        return str(display_error.ads_not_found_error(self.name))

class NotValidRuleset(Exception):
    """thrown when user attempts to import ruleset that's not correct format"""
    def __init__(self, name=None):
        self.name = name
    
    def __str__(self):
        from src.praxxis.display import display_error
        return str(display_error.invalid_ruleset_import(self.name))

class EmptyHistoryError(Exception):
    """thrown when history is empty, but op requires history"""
    def __init__(self):
        pass
    
    def __str__(self):
        from src.praxxis.display import display_error
        return str(display_error.empty_history_error())
