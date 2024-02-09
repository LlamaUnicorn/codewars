from hypothesis import given, example, strategies as st

from q8_Remove_String_Spaces import no_space


test_cases = {
    '4556364607935616': '############5616',
    '64607935616': '#######5616',
    '1': '1',
    '': '',
}


@given(st.sampled_from(list(test_cases.keys())))
def test_no_space_example(word):
    result = no_space(word)
    assert result == test_cases[word], f"Incorrect answer for \"{word}\""
