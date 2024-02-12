import string
from hypothesis.strategies import just, text, lists, integers

from hypothesis import given, example, strategies as st

from q6_Stop_gninnipS_My_sdroW import spin_words


test_cases = {
    'Hey fellow warriors': 'Hey wollef sroirraw',
    'This is a test': 'This is a test',
    'This is another test': 'This is rehtona test',
}


@given(st.sampled_from(list(test_cases.keys())))
def test_spin_words_example(word):
    result = spin_words(word)
    assert result == test_cases[word], f"Incorrect answer for \"{word}\""
