"""
This file is responsible for displaying messages to the console.
"""

def expand_list(list_data):
    """expands list of tuples for pretty printing"""
    return "\n\t".join(list(sum(list_data, ())))


def display_delete_env(name):
    """ the display function for deleted environments"""
    print(f"{name} deleted")


def display_list_env(envs):
    """the display function for listing environments"""
    print(f"Environment Variables: ")
    if envs == []:
        print("\tNone Set")
        return
    i = 0
    for env in envs:
        i += 1
        print(f"\t{i}.\t{env[0]} = {env[1]}")


def display_set_env(name, value):
    """the display function for set environments"""
    print(f"Set environment for scene:\n\t{name} = {value}")


def display_list_notebook(notebooks):
    """the display function for listing notebooks"""
    print(f"Notebooks:")
    i = 0
    for notebook in notebooks:
        i+=1
        print(f"\t{i}.\t{notebook[0]}")


def display_init_libraries_folder(root):
    """the display function for creating new libraries folder"""
    print(f"Created libraries directory at {root}")


def display_init_libraries_db(db_root):
    """the display function for initializing the libraries db"""
    print(f"Created libraries database at {db_root}")


def display_loaded_library(root, first):
    """the display function for loading libarires"""
    if first:
        print(f"Loaded library at:\n\t{root}")
    else:
        print(f"\t{root}")


def display_loaded_notebook(name, first):
    """the display function for loaded notebooks"""
    if first:
        print(f"Loaded notebook:\n\t{name}")
    else:
        print(f"\t{name}")


def display_libraries(libraries):
    """the display function for listing libraries""" 
    print(f"Loaded libraries:\n\t{expand_list(libraries)}")


def display_change_scene(name):
    """the display function for chaging scene name"""
    print(f"Scene changed to: {name}")


def display_current_scene(name):
    """the display function for showing the current scene""" 
    print(f"Current scene: {name}")


def display_init_scene_folder(root):
    """the display function for initializing the scene folder"""
    print(f"Created scenes directory at {root}")


def display_init_scene_db(db_root):
    """the display function for initializing the scene database"""
    print(f"Created history db at {db_root}")


def display_new_scene(name):
    """the display function for creating a new scene"""
    print(f"Created new scene \"{name}\"")


def display_delete_scene_success(name):
    """the display function for successfully deleting a scene""" 
    print(f"Deleted scene: {name}")


def display_end_scene_success(name):
    """the display function for ending a scene""" 
    print(f"{name} ended")


def display_list_scene(ended, active, current):
    """the display function for listing scenes""" 
    i = 0
    print(f"Ended scenes:")
    for scene in ended:
        i += 1
        print(f"\t{i}.\t{scene[0]}")
    if (len(ended) == 0):
        print(f"\tNone")
    print(f"\nActive scenes:")
    for scene in active:
        i += 1
        print(f"\t{i}.\t{scene[0]}")
    if (len(active) == 0):
        print(f"\tNone")
    print(f"\nCurrent scene: {current}")

def display_resume_scene(name):
    """the display function for resuming the scene""" 
    print(f"{name} resumed")


def display_run_notebook_start(notebook_name):
    """the beginning display function for running a notebook"""
    print(f"\nRunning {notebook_name}...\n")


def display_run_notebook_html(output_root, html_outfile):
    """the display function for running a notebook with html"""
    print("\nCOMPLETE\n")
    print("View HTML output from notebook runs here")
    print(f"\t{output_root}")
    print("Launching result file in web browser")
    print(f"\t{html_outfile}")


def display_run_notebook(filename):
    """the display function for running a notebook"""
    import nbconvert
    print("\nNotebook output:")
    
    output = nbconvert.exporters.export(nbconvert.MarkdownExporter(), filename)[0]


def display_init_run_notebook(outfile_root):
    """the display function for initializing the notebooks directory"""
    print(f"Created outfile directory at {outfile_root}")


def display_history(current_scene, notebooks):
    """the display function for showing the history of the current scene"""
    print(f"History for scene {current_scene}")
    print(f"\tTIMESTAMP\t\tNOTEBOOK\t\tLIBRARY")
    for notebook in notebooks:
        print(f"\t{notebook[0]}\t{notebook[1]}\t{notebook[2]}")


def display_search(search_term, notebooks):
    """the display function for showing the results of the current search"""
    print(f"Search notebook names for \"{search_term}\"")
    counter = 0
    for notebook in notebooks:
        counter += 1
        print(f"\t{counter}.\t{notebook[0]}")
    if len(notebooks) == 0:
        print("\tNo results found")


def scene_does_not_exist_error(name):
    """the error display for scenes not existing"""
    print(f"{name} does not exist")


def notebook_does_not_exist_error(name):
    """the error display for notebooks not existing"""
    print(f"{name} does not exist")


def last_active_scene_error(name):
    """the error display for trying to end the last active scene"""
    print(f"{name} is your last active scene. Make a new scene, or resume an old one.")


def env_not_found_error(name):
    """the error display for environments not being found"""
    print(f"{name} not found")


def scene_ended_error(name):
    """the error display for trying to switch to an ended scene"""
    print(f"can't switch to {name}, because the scene has ended. Resume the scene or make a new one")


def papermill_error(error):
        """the error display for papermill errors"""
        print("PAPERMILL ERROR")
        print(error)


def no_tagged_cell_warning():
    """the warning display for having no tagged cell"""
    print("Warning: no tagged cell located. No parameters will be injected for this notebook.")
    