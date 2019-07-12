"""
adds test library to temp directories and does a few useful operations on them
"""
import pytest

@pytest.fixture(scope="function")
def add_test_library(library_root, library_db):
    """
    copies test notebooks from the tests directory to the temp root, and loads them into the db
    """
    import os
    import shutil 
    from src.mtool.library import sync_library
    from src.mtool.library import remove_library
    from tests.src.mtool.util import dummy_object

    library_location = os.path.join(library_root, 'test_notebooks')
    
    shutil.copytree(os.path.join('tests', 'test_notebooks'), os.path.join(library_root,  'test_notebooks'))
    assert os.path.exists(library_location)

    sync_library.sync_libraries(library_root, library_db)   
    yield 
    dummy_library = dummy_object.make_dummy_library()
    remove_library.remove_library(dummy_library, library_db)
    shutil.rmtree(library_location)


@pytest.fixture
def libraries_list(library_root):
    """
    returns a list of libraries loaded
    """
    import os
    
    return(next(os.walk(library_root))[1])


@pytest.fixture(scope="session")
def notebooks_list():
    """
    returns a list of the notebooks loaded in the temp library
    """
    import os

    return(os.listdir(os.path.join('tests', 'test_notebooks')))
