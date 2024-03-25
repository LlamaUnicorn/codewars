from q6_Multiplication_table import multiplication_table
from hypothesis import given, example, strategies as st

test_cases = {
    3: [[1, 2, 3], [2, 4, 6], [3, 6, 9]],
}


@given(st.sampled_from(list(test_cases.keys())))
def test_multiplication_table_example(word):
    result = multiplication_table(word)
    assert result == test_cases[word], f"Incorrect answer for \"{word}\""
