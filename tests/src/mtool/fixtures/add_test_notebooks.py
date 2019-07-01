import pytest

@pytest.fixture(scope="session")
def add_test_notebooks(library_root):
    import os
    import shutil 

    library_location = os.path.join(library_root, 'test_notebooks')
    shutil.copytree(os.path.join('tests', 'test_notebooks'), os.path.join(library_root,  'test_notebooks'))
    assert os.path.exists(library_location)


@pytest.fixture(scope="session")
def notebooks_list(add_test_notebooks):
    import os

    return(os.listdir(os.path.join('tests', 'test_notebooks')))


@pytest.fixture(scope="session")
def libraries_list(library_root):
    import os
    
    return(next(os.walk(library_root))[1])