import os
import sys
from hypothesis import given, example, strategies as st
from hypothesis.strategies import just

from Strings.q7_vowel_count import get_count

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@given(just('aeiou'))
def test_all_vowels_get_count(words):
    result = get_count(words)
    assert result == 5, f"Incorrect answer for \"aeiou\""


#     assert all(len(word) > i for i, word in enumerate(words)) or result == ''
#     assert all(word[i] == result[i] for i, word in enumerate(words) if len(word) > i)
#
#
# @given(st.lists(st.text(), max_size=0))
# @example([])
# def test_empty_get_count(words):
#     assert get_count(words) == ''
#
#
# @given(st.lists(st.text(min_size=1), min_size=1, max_size=1))
# @example(['X-ray'])
# def test_dash_word_get_count(words):
#     assert get_count(words) == words[0][0]

# def test_get_count():
#     assert get_count(['yoda', 'best', 'has']) == 'yes'
#
#
# def test_empty_get_count():
#     assert get_count([]) == ''
#
#
# def test_dash_word_get_count():
#     assert get_count(['X-ray']) == 'X'
