import string
from hypothesis.strategies import just, text, lists, integers

from hypothesis import given, example, strategies as st

from q6_Highest_Scoring_Word import high


test_cases = {
    'man i need a taxi up to ubud': 'taxi',
    'what time are we climbing up the volcano': 'volcano',
    'b aa': 'b',
}


@given(st.sampled_from(list(test_cases.keys())))
def test_high_example(word):
    result = high(word)
    assert result == test_cases[word], f"Incorrect answer for \"{word}\""