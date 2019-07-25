"""
This file contains all of the display functions for notebooks
"""

def display_list_notebook(notebooks):
    """the display function for listing notebooks"""
    print(f"Notebooks:")
    i = 0
    library = ""
    for notebook in notebooks:
        if not library == notebook[2]:
            print(f"    {notebook[2]}:\n")
            library = notebook[2]
        i+=1
        print(f"\t{i}.\t{notebook[0]}")


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
    print(output)


def display_init_run_notebook(outfile_root):
    """the display function for initializing the notebooks directory"""
    print(f"Created outfile directory at {outfile_root}")


def display_search(search_term, notebooks):
    """the display function for showing the results of the current search"""
    print(f"Search notebook names for \"{search_term}\"")
    if len(notebooks) == 0:
        print("\tNo results found")
    else:
        display_list_notebook(notebooks)
    return notebooks


def display_remove_success(name):
    """the display function for removing a notebook sucessfullly"""
    print(f"Successfully removed notebook {name}")
