from hypothesis import given, example, strategies as st

from q7_String_ends_with import solution


test_cases = [
    ('abc', 'bc', True),
    ('abc', 'd', False),
    # Add more test cases as needed
]


@given(st.sampled_from(test_cases))
def test_solution_example(test_case):
    str1, str2, expected = test_case
    result = solution(str1, str2)
    assert result == expected, f"Incorrect answer for \"{str1}\", \"{str2}\""
