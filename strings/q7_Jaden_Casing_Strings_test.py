import string
from hypothesis.strategies import just, text, lists, integers

from hypothesis import given, example, strategies as st

from q7_Jaden_Casing_Strings import to_jaden_case


test_cases = {
    # 'what you pass': 'what you expect',
    'How can mirrors be real if our eyes aren\'t real': 'How Can Mirrors Be Real If Our Eyes Aren\'t Real',
    'most trees are blue': 'Most Trees Are Blue',
}


@given(st.sampled_from(list(test_cases.keys())))
def test_is_jaden_case_example(word):
    print(f'{word=}')
    result = to_jaden_case(word)
    assert result == test_cases[word], f"Incorrect answer for \"{word}\""