from hypothesis import given, strategies as st

from q8_Convert_number_to_reversed_array_of_digits import digitize

test_cases = {
    35231: [1, 3, 2, 5, 3],
    0: [0],
}


@given(st.sampled_from(list(test_cases.keys())))
def test_digitize_example(word):
    result = digitize(word)
    assert result == test_cases[word], f"Incorrect answer for \"{word}\""
