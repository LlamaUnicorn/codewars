import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from head_tail_init_and_last import head, tail, init, last

# @pytest.mark.parametrize("lst, expected", [1, 2, 3, 4, 5,])

def test_head(lst):
    assert head(lst) == 1

def test_tail(lst):
    assert tail(lst) == [2,3,4,5]

def test_init(lst):
    assert init(lst) == [1,2,3,4]

def test_last(lst):
    assert last(lst) == 5


@pytest.fixture
def lst():
    return [1, 2, 3, 4, 5]
