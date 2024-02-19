import string
from hypothesis.strategies import just, text, lists, integers

from hypothesis import given, example, strategies as st

from q8_Square_n_Sum import square_sum

test_cases = {
    (1, 2, 2): 9,
}


def test_positive_sum():
    for names, expected in test_cases.items():
        result = square_sum(names)
        assert result == expected, f"Incorrect answer for \"{names}\""