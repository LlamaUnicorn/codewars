import string
from hypothesis.strategies import just, text, lists, integers

from hypothesis import given, example, strategies as st

from q6_Counting_Duplicates import duplicate_count


test_cases = {
    'abcde': 0,
    'aabbcde': 2,
    'aabBcde': 2,
    'indivisibility': 1,
    'Indivisibilities': 2,
    'aA11': 2,
    'ABBA': 2,
}


@given(st.sampled_from(list(test_cases.keys())))
def test_duplicate_count_example(word):
    print(word)
    result = duplicate_count(word)
    assert result == test_cases[word], f"Incorrect answer for \"{word}\""
