import os
import sys
import string
from hypothesis.strategies import just, text, lists, integers

from hypothesis import given, example, strategies as st

from Strings.q7_Isograms import is_isogram

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


test_cases = {
    'Dermatoglyphics': True,
    'isogram': True,
    'thumbscrew-japingly': True,
    'hello': False,
    'world': True,
    'aba': False,
    # 'moOse': False,
}


@given(st.sampled_from(list(test_cases.keys())))
def test_is_isogram_example(word):
    result = is_isogram(word)
    assert result == test_cases[word], f"Incorrect answer for \"{word}\""


@given(just(''))
def test_is_isogram_empty(word):
    result = is_isogram(word)
    assert result == True, f"Incorrect answer for \"{word}\""


def is_isogram_reference_implementation(word):
    return len(word) == len(set(word.lower()))


@given(st.text(alphabet=string.ascii_letters, min_size=2))
# @example('Aa')
def test_is_isogram(word):
    print(f'Testing with word: {word}')
    result = is_isogram(word)
    expected = is_isogram_reference_implementation(word)
    assert result == expected, f"Incorrect answer for \"{word}\""

# @given(st.text(alphabet=string.ascii_letters, min_size=1))

# def test_is_isogram(word):
#     result = is_isogram(word)
#     expected = is_isogram_reference_implementation(word)
#     assert result == expected, f"Incorrect answer for \"{word}\""