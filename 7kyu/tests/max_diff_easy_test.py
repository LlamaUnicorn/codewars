import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from max_diff_easy import max_diff


@pytest.mark.parametrize("lst, expected", [
    ([], 0),
    ([5], 0),
    ([1, 2, 3, 4], 3),
    ([1, 2, 3, -4], 7),
    ([0, 1, 2, 3, 4, 5, 6], 6),
])

def test_max_diff(lst, expected):
    assert max_diff(lst) == expected
