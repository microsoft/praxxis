class NotebookNotFoundError(Exception):
    def __init__(self, name=None):
        self.name = name


    def __str__(self):
        from src.praxxis.display import display_error
        return str(display_error.notebook_not_found_error(self.name))

class RuleNotFoundError(Exception):
    def __init__(self, name=None):
        self.name = name


    def __str__(self):
        from src.praxxis.display import display_error
        return str(display_error.rule_not_found_error(self.name))

class RulesetNotFoundError(Exception):
    def __init__(self, name=None):
        self.name = name

    def __str__(self):
        from src.praxxis.display import display_error
        return str(display_error.ruleset_not_found_error(self.name))

class RulesetActiveError(Exception):
    def __init__(self, name=None):
        self.name = name

    def __str__(self):
        from src.praxxis.display import display_error
        return str(display_error.ruleset_active_error(self.name))

class RulesetNotActiveError(Exception):
    def __init__(self, name=None):
        self.name = name

    def __str__(self):
        from src.praxxis.display import display_error
        return str(display_error.ruleset_not_active_error(self.name))

class ParamNotFoundError(Exception):
    def __init__(self, name=None):
        self.name = name
    

    def __str__(self):
        from src.praxxis.display import display_error
        return str(display_error.param_not_found_error(self.name))


class SceneNotFoundError(Exception):
    def __init__(self, name=None):
        self.name = name
    

    def __str__(self):
        from src.praxxis.display import display_error
        return str(display_error.scene_not_found_error(self.name))


class SceneEndedError(Exception):
    def __init__(self, name=None):
        self.name = name
    

    def __str__(self):
        from src.praxxis.display import display_error
        return str(display_error.scene_ended_error(self.name))


class LastActiveSceneError(Exception):    
    def __init__(self, name=None):
        self.name = name
    

    def __str__(self):
        from src.praxxis.display import display_error
        return str(display_error.last_active_scene_error(self.name))


class EndEndedSceneError(Exception):
    def __init__(self, name=None):
        self.name = name
    
    def __str__(self):
        from src.praxxis.display import display_error
        return str(display_error.end_ended_scene_error(self.name))


class LibraryNotFoundError(Exception):
    def __init__(self, name=None):
        self.name = name
    
    def __str__(self):
        from src.praxxis.display import display_error
        return str(display_error.library_not_found_error(self.name))


class NotDirectoryError(Exception):
    def __init__(self, name=None):
        self.name = name
    
    def __str__(self):
        from src.praxxis.display import display_error
        return str(display_error.not_directory_error(self.name))

    
class NotFileError(Exception):
    def __init__(self, name=None):
        self.name = name
    
    def __str__(self):
        from src.praxxis.display import display_error
        return str(display_error.not_file_error(self.name))


class NotNotebookError(Exception):
    def __init__(self, name=None):
        self.name = name
    
    def __str__(self):
        from src.praxxis.display import display_error
        return str(display_error.not_notebook_error(self.name))


class DuplicateNotebookError(Exception):
    def __init__(self, name=None):
        self.name = name
    

    def __str__(self):
        from src.praxxis.display import display_error
        return str(display_error.duplicate_notebook_error(self.name))


class EditorNotFoundError(Exception):
    def __init__(self, name=None):
        self.name = name
    
    def __str__(self):
        from src.praxxis.display import display_error
        return str(display_error.editor_not_found_error(self.name))


class ADSNotFoundError(Exception):
    def __init__(self, name=None):
        self.name = name
    
    def __str__(self):
        from src.praxxis.display import display_error
        return str(display_error.ads_not_found_error(self.name))

class NotValidRuleset(Exception):
    def __init__(self, name=None):
        self.name = name
    
    def __str__(self):
        from src.praxxis.display import display_error
        return str(display_error.invalid_ruleset_import(self.name))

class EmptyHistoryError(Exception):
    def __init__(self):
        pass
    
    def __str__(self):
        from src.praxxis.display import display_error
        return str(display_error.empty_history_error())
