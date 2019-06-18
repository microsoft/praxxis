from src.mtool.cli import display

def test_expand_list(list_data):
    display.expand_list(list_data)


def test_display_delete_env(name):
    display.display_delete_env(name)


def test_display_list_env(envs):
    display.display_list_env(envs)


def test_display_set_env(name, value):
    display.display_set_env(name, value)


def test_display_list_notebook(notebooks):
    display.display_list_notebook(notebooks)


def test_display_init_libraries_folder(root):
    display.display_init_libraries_folder(root)


def test_display_init_libraries_db(db_root):
    display.display_init_libraries_db(db_root)


def test_display_loaded_library(root, first):
    display.display_loaded_library(root, first)


def test_display_loaded_notebook(name, first):
    display.display_loaded_notebook(name, first)


def test_display_libraries(libraries):
    display.display_libraries(libraries)


def test_display_change_scene(name):
    display.display_change_scene(name)


def test_display_init_scene_folder(root):
    display.display_init_scene_folder(root)


def test_display_init_scene_db(db_root):
    display.display_init_scene_db(db_root)


def test_display_new_scene(name):
    display.display_new_scene(name)


def test_display_delete_scene_success(name):
    display.display_delete_scene_success(name)


def test_display_end_scene_success(name):
    display.display_end_scene_success(name)


def test_display_list_scene(ended, active, current):
    display.display_list_scene(ended, active, current)


def test_display_resume_scene(name):
    display.display_resume_scene(name)


def test_display_run_notebook_start(notebook_name):
    display.display_run_notebook_start(notebook_name)


def test_display_run_notebook_html(output_root, html_outfile):
    display.display_run_notebook_html(output_root, html_outfile)


def test_display_run_notebook(filename):
    display.display_run_notebook(filename)


def test_display_init_run_notebook(outfile_root):
    display.display_init_run_notebook(outfile_root)


def test_display_history(current_scene, notebooks):
    display.display_history(current_scene, notebooks)


def test_display_search(search_term, notebooks):
    display.display_search(search_term, notebooks)


def test_secene_does_not_exist_error(name):
    display.scene_does_not_exist_error(name)


def test_notebook_does_not_exist_error(name):
    display.notebook_does_not_exist_error(name)


def test_last_active_scene_error(name):
    display.last_active_scene_error(name)


def test_env_not_found_error(name):
    display.env_not_found_error(name)


def test_scene_ended_error(name):
    display.scene_ended_error(name)


def test_papermill_error(error):
    display.papermill_error(error)


def test_no_tagged_cell_warning():
    display.no_tagged_cell_warning()