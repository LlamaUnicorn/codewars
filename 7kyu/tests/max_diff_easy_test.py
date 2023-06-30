import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from max_diff_easy import add_numbers

def test_add_numbers():
    assert add_numbers(2, 3) == 5
