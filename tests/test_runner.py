import pytest

def test_run_notebook():
    from src.mtool.app import run_notebook
    print("run_notebook")

def test_open_notebook():
    from src.mtool.app import open_notebook
    print("open_notebook")

def test_search_notebook():
    from src.mtool.app  import search_notebook
    print("search_notebook")

def test_list_notebook():
    from src.mtool.app  import list_notebook
    print("list_notebook")

def test_history():
    from src.mtool.app  import history
    print("history")

def test_next_notebook():
    from src.mtool.app  import next_notebook
    print("next_notebook")

def test_new_scene():
    from src.mtool.app  import new_scene
    print("new_scene")

def test_end_scene():
    from src.mtool.app  import end_scene
    print("end_scene")

def test_resume_scene():
    from src.mtool.app  import resume_scene
    print("resume_scene")

def test_delete_scene():
    from src.mtool.app  import delete_scene
    print("delete_scene")

def test_list_scene():
    from src.mtool.app  import list_scene
    print("list_scene")

def test_add_library():
    from src.mtool.app  import add_library
    print("add_library")

def test_list_library():
    from src.mtool.app  import list_library
    print("list_library")

def test_set_env():
    from src.mtool.app  import set_env
    print("set_env")

def test_delete_env():
    from src.mtool.app  import delete_env
    print("delete_env")
