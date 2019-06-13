def explode_list(list_data):
    return "\n\t".join(list(sum(list_data, ())))


def display_delete_env(name):
    print(f"{name} deleted")


def display_list_env(envs):
    print(explode_list(envs))


def display_set_env(name, value):
    print(f"Set environment for scene:\n\t{name} = {value}")


def display_list_notebook(notebooks):
    print(f"Notebooks:\n\t{explode_list(notebooks)}")


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


def scene_does_not_exist_error(name):
    print(f"{name} does not exist")


def last_active_scene_error(name):
    print(f"{name} is your last active scene. Make a new scene, or restart an old one.")


def display_end_scene_success(name):
    print(f"{name} ended")