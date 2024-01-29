import os
import sys
from hypothesis import given, example, strategies as st
from hypothesis.strategies import just, text

from Strings.q7_Highest_and_Lowest import high_and_low

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@given(just('8 3 -5 42 -1 0 0 -9 4 7 4 -4'))
def test_high_and_low(words):
    result = high_and_low(words)
    assert result == '42 -9', f"Incorrect answer for \"8 3 -5 42 -1 0 0 -9 4 7 4 -4\""


# @given(just('y'))
# def test_no_vowels_get_count(words):
#     result = high_and_low(words)
#     assert result == 0, f"Incorrect answer for \"y\""
#
#
# @given(text())
# def test_generated_get_count(words):
#     result = high_and_low(words)
#     expected = sum(1 for char in words if char in 'aeiou')
#     assert result == expected, f"Incorrect answer for \"generator\""
