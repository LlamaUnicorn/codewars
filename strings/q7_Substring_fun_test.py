import os
import sys
from hypothesis import given, example, strategies as st

from q7_Substring_fun import nth_char

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@given(st.lists(st.text(min_size=1), min_size=1))
@example(['yoda', 'best', 'has'])
def test_nth_char(words):
    result = nth_char(words)
    assert all(len(word) > i for i, word in enumerate(words)) or result == ''
    assert all(word[i] == result[i] for i, word in enumerate(words) if len(word) > i)


@given(st.lists(st.text(), max_size=0))
@example([])
def test_empty_nth_char(words):
    assert nth_char(words) == ''


@given(st.lists(st.text(min_size=1), min_size=1, max_size=1))
@example(['X-ray'])
def test_dash_word_nth_char(words):
    assert nth_char(words) == words[0][0]

# def test_nth_char():
#     assert nth_char(['yoda', 'best', 'has']) == 'yes'
#
#
# def test_empty_nth_char():
#     assert nth_char([]) == ''
#
#
# def test_dash_word_nth_char():
#     assert nth_char(['X-ray']) == 'X'
