import pytest

def test_add_regular_library(setup, library_db, git_root, start, stop):
    from src.praxxis.library import add_library
    from src.praxxis.library import list_library
    from src.praxxis.library import remove_library
    from tests.src.praxxis.util import dummy_object

    library_path = dummy_object.make_dummy_library_path()
    library = dummy_object.make_dummy_library()

    add_library.add_library(library_path, library_db, git_root)

    libraries = list_library.list_library(library_db, start, stop)
    assert len(libraries) == 1
    remove_library.remove_library(library, library_db, start, stop)
    libraries = list_library.list_library(library_db, start, stop)
    assert len(libraries) == 0

@pytest.mark.skip(reason="need to decide on a good git repo to test this on ")
def test_add_git_library(setup, library_db, git_root, start, stop):
    from src.praxxis.library import add_library
    from src.praxxis.library import remove_library
    from src.praxxis.library import list_library
    from tests.src.praxxis.util import dummy_object
    from src.praxxis.util import rmtree

    url = dummy_object.make_dummy_git_repo()
    add_library.add_library(url, library_db, git_root)

    libraries = list_library.list_library(library_db, start, stop)
    assert len(libraries) == 1
    remove_library.remove_library(url, library_db, start, stop)
    libraries = list_library.list_library(library_db, start, stop)

    assert len(libraries) == 0
    rmtree.rmtree(git_root, test=True)


def test_add_bad_library(setup, library_db, git_root, start, stop):
    from src.praxxis.library import add_library
    from tests.src.praxxis.util import dummy_object
    from src.praxxis.util import error
    from src.praxxis.display import display_error

    url = dummy_object.make_dummy_object(name="nonexistent_library")
    try:
        add_library.add_library(url, library_db, git_root)
    except error.LibraryNotFoundError as e:
        assert str(e) == display_error.library_not_found_error(url.library_name)
    else:
        assert 0
