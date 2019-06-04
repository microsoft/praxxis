@ECHO OFF
CALL python ..\runner.py "diagnose" "me"
CALL python ..\runner.py "run_notebook" "notebook"
CALL python ..\runner.py "open_notebook" "this notebook"
CALL python ..\runner.py "search_notebook" "SOP"
CALL python ..\runner.py "list_notebook" 
CALL python ..\runner.py "history" 
CALL python ..\runner.py "next_notebook" 
CALL python ..\runner.py "new_scene" 
CALL python ..\runner.py "end_scene" 
CALL python ..\runner.py "change_scene" 
CALL python ..\runner.py "resume_scene" 
CALL python ..\runner.py "delete_scene" 
CALL python ..\runner.py "list_scene" 
CALL python ..\runner.py "add_library" 
CALL python ..\runner.py "set_env" 
CALL python ..\runner.py "delete_env" 



