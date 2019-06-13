def explode_list(list_data):
    return "\n\t".join(list(sum(list_data, ())))

def explode_zipped_list(list_data):
    return (f"\n\t".join(list(zip(*list_data))[0]))

def explode_scenes_list(list_data):
    return list(sum(list_data, ()))

def display_delete_env(name):
    print(f"{name} deleted")


def display_list_env(envs):
    print(f"Environment Variables: ")
    if envs == []:
        print("\tNone Set")
        return
    i = 0
    for env in envs:
        i += 1
        print(f"{i}\t{env[0]} = {env[1]}")


def display_set_env(name, value):
    print(f"Set environment for scene:\n\t{name} = {value}")


def display_list_notebook(notebooks):
    print(f"Notebooks:")
    i = 0
    for notebook in notebooks:
        i+=1
        print(f"{i}\t{notebook[0]}")


def display_init_libraries_folder(root):
    print(f"Created libraries directory at {root}")


def display_init_libraries_db(db_root):
    print(f"Created libraries database at {db_root}")


def display_loaded_library(root, first):
    if first:
        print(f"Loaded library at:\n\t{root}")
    else:
        print(f"\t{root}")


def display_loaded_notebook(name, first):
    if first:
        print(f"Loaded notebook:\n\t{name}")
    else:
        print(f"\t{name}")


def display_libraries(libraries):
    print(f"Loaded libraries:\n\t{explode_list(libraries)}")


def display_change_scene(name):
    print(f"Scene changed to: {name}")


def display_current_scene(name):
    print(f"Current scene: {name}")


def display_init_scene_folder(root):
    print(f"Created scenes directory at {root}")


def display_init_scene_db(db_root):
    print(f"Created history db at {db_root}")


def display_new_scene(name):
    print(f"Created new scene \"{name}\"")


def display_delete_scene_success(name):
    print(f"Deleted scene: {name}")


def display_end_scene_success(name):
    print(f"{name} ended")


def display_list_scene(ended, active, current):
    i = 0
    
    print(f"Ended scenes:")
    for scene in ended:
        i += 1
        print(f"{i}\t{scene[0]}")
    print(f"Active scenes:")
    for scene in active:
        i += 1
        print(f"{i}\t{scene[0]}")
    print(f"Current scene:")
    i += 1
    print(f"{i}\t{current}")

def display_resume_scene(name):
    print(f"{name} resumed")


def scene_does_not_exist_error(name):
    print(f"{name} does not exist")


def notebook_does_not_exist_error(name):
    print(f"{name} does not exist")


def last_active_scene_error(name):
    print(f"{name} is your last active scene. Make a new scene, or restart an old one.")


def env_not_found_error(name):
    print(f"{name} not found")


def no_tagged_cell_warning():
    print("Warning: no tagged cell located. No parameters will be injected for this notebook.")

def display_run_notebook_start(notebook_name):
    print(f"\nRunning {notebook_name}...\n")

def display_run_notebook_html(output_root, html_outfile):
    print("\nCOMPLETE\n")
    print("View HTML output from notebook runs here")
    print(f"\t{output_root}")
    print("Launching result file in web browser")
    print(f"\t{html_outfile}")

def display_run_notebook(filename):
    import pypandoc
    print("\nNotebook output:")
    print(pypandoc.convert_file(filename, 'asciidoc'))

def display_init_run_notebook(outfile_root):
    print(f"Created outfile directory at {outfile_root}")
