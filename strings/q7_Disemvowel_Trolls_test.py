from hypothesis import given
from hypothesis.strategies import just

from q7_Disemvowel_Trolls import disemvowel


@given(just('You should leave'))
def test_all_vowels_get_count(words):
    result = disemvowel(words)
    assert result == 'Y shld lv', f"Incorrect answer for \"You should leave\""
