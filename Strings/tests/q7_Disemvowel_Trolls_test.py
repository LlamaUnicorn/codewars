import os
import sys

from hypothesis import given
from hypothesis.strategies import just

from Strings.q7_Disemvowel_Trolls import disemvowel

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@given(just('You should leave'))
def test_all_vowels_get_count(words):
    result = disemvowel(words)
    assert result == 'Y shld lv', f"Incorrect answer for \"You should leave\""
