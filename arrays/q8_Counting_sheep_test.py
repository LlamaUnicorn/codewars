from hypothesis import given, strategies as st

from q8_Counting_sheep import count_sheeps

test_cases = {
    (True, True, True, False,
     True, True, True, True,
     True, False, True, False,
     True, False, False, True,
     True, True, True, True,
     False, False, True, True): 17,
}


@given(st.sampled_from(list(test_cases.keys())))
def test_count_sheeps_example(word):
    result = count_sheeps(word)
    assert result == test_cases[word], f"Incorrect answer for \"{word}\""
