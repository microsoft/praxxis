from src.mtool.cli import function_switcher

def test_get_current_scene_db():
    function_switcher.get_current_scene_db()


def test_run_notebook(arg):
    function_switcher.run_notebook(arg)


def test_open_notebook(arg):
    function_switcher.open_notebook(arg)


def test_search_notebook(arg):
    function_switcher.search_notebook(arg)


def test_list_notebook(arg):
    function_switcher.list_notebook(arg)


def test_next_notebook(arg):
    function_switcher.next_notebook(arg)


def test_history(arg):
    function_switcher.history(arg)


def test_new_scene(arg):
    function_switcher.new_scene(arg)


def test_end_scene(arg):
    function_switcher.end_scene(arg)


def test_change_scene(arg):
    function_switcher.change_scene(arg)


def test_resume_scene(arg):
    function_switcher.resume_scene(arg)


def test_delete_scene(arg):
    function_switcher.delete_scene(arg)


def test_list_scene(arg):
    function_switcher.list_scene(arg)


def test_set_env(arg):
    function_switcher.set_env(arg)


def test_delete_env(arg):
    function_switcher.delete_env(arg)


def test_list_env(arg):
    function_switcher.list_env(arg)


def test_add_library(arg):
    function_switcher.add_library(arg)


def test_list_library(arg):
    function_switcher.list_library(arg)


def test_load_library(arg):
    function_switcher.load_library(arg)


def test_default(arg):
    function_switcher.default(arg)


def test_command(arg):
    function_switcher.command(arg)
    