from src.mtool.cli import function_switcher

def test_run_notebook():
    function_switcher.run_notebook
    print("run_notebook")

def test_open_notebook():
    function_switcher.open_notebook
    print("open_notebook")

def test_search_notebook():
    function_switcher.search_notebook
    print("search_notebook")

def test_list_notebook():
    function_switcher.list_notebook
    print("list_notebook")

def test_history():
    function_switcher.history
    print("history")

def test_next_notebook():
    function_switcher.next_notebook
    print("next_notebook")

def test_new_scene():
    function_switcher.new_scene
    print("new_scene")

def test_end_scene():
    function_switcher.end_scene
    print("end_scene")

def test_resume_scene():
    function_switcher.resume_scene
    print("resume_scene")

def test_delete_scene():
    function_switcher.delete_scene
    print("delete_scene")

def test_list_scene():
    function_switcher.list_scene
    print("list_scene")

def test_add_library():
    function_switcher.add_library
    print("add_library")

def test_list_library():
    function_switcher.list_library
    print("list_library")

def test_set_env():
    function_switcher.set_env
    print("set_env")

def test_delete_env():
    function_switcher.delete_env
    print("delete_env")
