from src.mtool.notebook import search_notebook

def test_search_notebook(args, library_db, start, end):
    search_notebook.search_notebook(args, library_db, start, end)