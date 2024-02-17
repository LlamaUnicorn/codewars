from hypothesis import given, strategies as st

from q6_Duplicate_Encoder import duplicate_encode


test_cases = {
    'din': "(((",
    'recede': "()()()",
    'Success': ")())())",
    '(( @': "))((",
    # '))))))': ")))))(",
}


@given(st.sampled_from(list(test_cases.keys())))
def test_duplicate_encode_example(word):
    result = duplicate_encode(word)
    assert result == test_cases[word], f"Incorrect answer for \"{word}\""
