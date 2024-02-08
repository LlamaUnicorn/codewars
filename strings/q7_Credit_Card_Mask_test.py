import string
from hypothesis.strategies import just, text, lists, integers

from hypothesis import given, example, strategies as st

from q7_Credit_Card_Mask import maskify


test_cases = {
    '4556364607935616': '############5616',
    '64607935616': '#######5616',
    '1': '1',
    '': '',
}


@given(st.sampled_from(list(test_cases.keys())))
def test_maskify_example(word):
    result = maskify(word)
    assert result == test_cases[word], f"Incorrect answer for \"{word}\""


# @given(st.text(alphabet=string.ascii_letters, min_size=1))
# def test_maskify_generator(word):
#     result = maskify(word)
#     expected_result = 'maskify(word)'
#     assert result == expected_result, f"Incorrect answer for \"{word}\""
