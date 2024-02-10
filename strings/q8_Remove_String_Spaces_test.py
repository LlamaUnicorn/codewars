from hypothesis import given, example, strategies as st

from q8_Remove_String_Spaces import no_space


test_cases = {
    '8 j 8   mBliB8g  imjB8B8  jl  B': '8j8mBliB8gimjB8B8jlB',
    '8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd': '88Bifk8hB8BB8BBBB888chl8BhBfd',
    '8aaaaa dddd r     ': '8aaaaaddddr',
}


@given(st.sampled_from(list(test_cases.keys())))
def test_no_space_example(word):
    result = no_space(word)
    assert result == test_cases[word], f"Incorrect answer for \"{word}\""
