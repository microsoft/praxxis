from src.mtool.notebook import notebook

def test_init_notebook_run(outfile_root):
    notebook.init_notebook_run(outfile_root)


def test_get_notebook_by_ordinal(scene_db, name):
    notebook.get_notebook_by_ordinal(scene_db, name)


def test_Notebook(notebook_data, library_path, openFile):
    Notebook = notebook.Notebook(notebook_data, library_path)

    Notebook.getpath()
    Notebook.extract_params(openFile)
    Notebook.extract_envVars(openFile)
