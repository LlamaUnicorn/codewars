import string
from hypothesis.strategies import just, text, lists, integers

from hypothesis import given, example, strategies as st

from q7_Sum_of_odd_numbers import row_sum_odd_numbers


test_cases = {
    1: 1,
    2: 8,
}


@given(st.sampled_from(list(test_cases.keys())))
def test_row_sum_odd_numbers_example(word):
    result = row_sum_odd_numbers(word)
    assert result == test_cases[word], f"Incorrect answer for \"{word}\""
