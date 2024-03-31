import string
from hypothesis.strategies import just, text, lists, integers

from hypothesis import given, example, strategies as st

from q6_Encrypt_this import encrypt_this


test_cases = {
    'Hello': "72olle",
    'good': "103doo",
    'hello world': "104olle 119drlo",
}


@given(st.sampled_from(list(test_cases.keys())))
def test_encrypt_this_example(word):
    result = encrypt_this(word)
    assert result == test_cases[word], f"Incorrect answer for \"{word}\""