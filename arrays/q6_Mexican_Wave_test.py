from hypothesis import given, strategies as st

from q6_Mexican_Wave import wave

test_cases = {
    'hello': ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
}


@given(st.sampled_from(list(test_cases.keys())))
def test_is_isogram_example(word):
    result = wave(word)
    assert result == test_cases[word], f"Incorrect answer for \"{word}\""
