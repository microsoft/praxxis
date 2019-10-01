"""
This file contains all of the display functions for notebooks
"""


def display_list_notebook(notebooks):
    """display function for listing notebooks"""
    print("Notebooks:")
    i = 0
    library = ""
    for notebook in notebooks:
        if not library == notebook[2]:
            print("    %s:" %(notebook[2])) 
            library = notebook[2]
        i+=1
        print("\t%s.\t%s"  %(i, notebook[0]))


def get_notebook_selection():
    """prompts user for notebook selection"""
    return input("")


def display_run_notebook_start(notebook_name):
    """beginning display function for running a notebook"""
    print("\nRunning %s...\n"  %(notebook_name))


def display_run_notebook_html(output_root, html_output):
    """display function for running a notebook with html"""
    print("\nCOMPLETE\n")
    print("View HTML output from notebook runs here")
    print("\t%s" %(output_root)) 
    print("Launching result file in web browser")
    print("\t%s" %(html_output)) 


def display_run_notebook(filename):
    """display function for running a notebook"""
    import nbconvert
    print("\nNotebook output:")
    
    output = nbconvert.exporters.export(nbconvert.MarkdownExporter(), filename)[0]
    print(output)


def display_init_run_notebook(output_root):
    """display function for initializing the notebooks directory"""
    print("Created output directory at %s" %(output_root)) 


def display_search(search_term, notebooks):
    """display function for showing the results of the current search"""
    print("Search notebook names for \"%s\"" %(search_term)) 
    if len(notebooks) == 0:
        print("\tNo results found")
    else:
        display_list_notebook(notebooks)
    return notebooks


def display_remove_success(name):
    """display function for removing a notebook sucessfullly"""
    print("Successfully removed notebook %s"  %(name))


def display_adding_output(name, output_string):
    """display function for adding output manually to a notebook execution"""
    print("For the last notebook executed (%s), added to the output \"%s\""  %(name, output_string))
