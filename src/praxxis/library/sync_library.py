"""
    This file loads libraries into the library database file
"""

import os

def sync_library(library_root, library_db, custom_path = False, remote = None, remote_origin = None):
    from src.praxxis.sqlite import sqlite_library
    from src.praxxis.util import error
    from src.praxxis.display import display_error
    from src.praxxis.notebook import notebook
    from src.praxxis.display import display_library
    from src.praxxis.sqlite import sqlite_parameter
    from src.praxxis.util import get_raw_git_url
    import os

    for root, dirs, files in os.walk(library_root):
        current_library = ""
        for name in files:
            if custom_path:
                relative_path = library_root
            else:
                relative_path = root.split(os.path.sep)[len(library_root.split(os.path.sep)):]
            library_name ="_".join(relative_path)

            print(relative_path)
            
            if relative_path == []:
                continue

            if not library_name == current_library:
                display_library.display_loaded_library(root, True)
                display_library.loaded_notebook_message()
                current_library = library_name

            readme_location = os.path.join(root, "README.md")
            readme_data = None

            if os.path.isfile(readme_location):
                f = open(readme_location, "r")
                readme_data = "  ".join(f.readlines()[:3])

            counter = 0
            try:
                library_metadata = sqlite_library.get_library_metadata(library_db, library_name)
                if not len(library_metadata) == 0:
                    if(root != library_metadata[0][0]):
                        while sqlite_library.check_library_exists(library_db, library_name):
                            library_name = f"{library_name}-{counter + 1}"
            except error.LibraryNotFoundError:
                pass


            file_name, file_extension = os.path.splitext(name)
            if(file_extension == ".ipynb"):
                file_root = os.path.join(root, name)
                        
                sqlite_library.sync_library(library_db, root, readme_data, library_name, remote)

                notebook_data = notebook.Notebook([file_root, file_name, library_name])
                #create a notebook object out of the file data
                for parameter in notebook_data._parameters:
                    #load the parameters out of the notebook object and into the db
                    sqlite_parameter.set_notebook_parameters(library_db, file_name, parameter[0].strip(), parameter[1], library_name)
                display_library.display_loaded_notebook(name)

                library_url = ("/").join(relative_path)
                raw_url = get_raw_git_url.get_raw_url_for_file(remote_origin, name, f"/{library_url}/")
                sqlite_library.load_notebook(library_db, file_root, file_name, library_name, raw_url)
