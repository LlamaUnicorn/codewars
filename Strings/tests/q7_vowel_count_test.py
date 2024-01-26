import os
import sys
from hypothesis import given, example, strategies as st
from hypothesis.strategies import just, text

from Strings.q7_vowel_count import get_count

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@given(just('aeiou'))
def test_all_vowels_get_count(words):
    result = get_count(words)
    assert result == 5, f"Incorrect answer for \"aeiou\""


@given(just('y'))
def test_no_vowels_get_count(words):
    result = get_count(words)
    assert result == 0, f"Incorrect answer for \"y\""


@given(text())
def test_generated_get_count(words):
    result = get_count(words)
    expected = sum(1 for char in words if char in 'aeiou')
    assert result == expected, f"Incorrect answer for \"generator\""

