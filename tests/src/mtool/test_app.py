from src.mtool import app
import sys
import pytest

def test_0_args():
    """
    this tests the 0 args command.
    this should have no command, since the 0 args case gets handled manually
    """
    namespace = app.main([])
    assert namespace.command == None


def test_list():
    """
    tests if the list command is running properly 
    """
    namespace = app.main(['l'])
    assert namespace.command == 'l'
    assert namespace.which == "list_notebooks"
