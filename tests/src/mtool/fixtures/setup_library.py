"""
adds test library to temp directories and does a few useful operations on them
"""
import pytest

@pytest.fixture(scope="session")
def add_test_library(library_root):
    """
    copies test notebooks from the tests directory to the temp root 
    """
    import os
    import shutil 

    library_location = os.path.join(library_root, 'test_notebooks')
    shutil.copytree(os.path.join('tests', 'test_notebooks'), os.path.join(library_root,  'test_notebooks'))
    assert os.path.exists(library_location)


@pytest.fixture(scope="session")
def notebooks_list(add_test_library):
    """
    returns a list of the notebooks loaded in the temp library
    """
    import os

    return(os.listdir(os.path.join('tests', 'test_notebooks')))


@pytest.fixture(scope="session")
def libraries_list(library_root):
    """
    returns a list of libraries loaded
    """
    import os
    
    return(next(os.walk(library_root))[1])