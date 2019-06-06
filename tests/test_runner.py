import pytest
from src.app import run_notebook

@pytest.mark.parametrize("param1, param2", [(3, 6)])
def test_generative(param1, param2):
    assert param1 * 2 < param2

def test_run():
    run_notebook("a")