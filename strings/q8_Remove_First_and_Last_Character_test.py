import string
from hypothesis.strategies import just, text, lists, integers

from hypothesis import given, example, strategies as st

from q8_Remove_First_and_Last_Character import remove_char


test_cases = {
    'eloquent': 'loquen',
    'country': 'ountr',
    'person': 'erso',
    'place': 'lac',
    'ok': '',
    'ooopsss': 'oopss',
}


@given(st.sampled_from(list(test_cases.keys())))
def test_remove_char_example(word):
    result = remove_char(word)
    assert result == test_cases[word], f"Incorrect answer for \"{word}\""


@given(st.text(alphabet=string.ascii_letters, min_size=1))
def test_remove_char_generator(word):
    result = remove_char(word)
    expected_result = word[1:-1] if len(word) > 1 else ""
    assert result == expected_result, f"Incorrect answer for \"{word}\""
