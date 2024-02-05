from hypothesis.strategies import just, text, lists, integers
from hypothesis import given, example, strategies as st
from q7_Highest_and_Lowest import high_and_low


@given(just('8 3 -5 42 -1 0 0 -9 4 7 4 -4'))
def test_high_and_low_example(numbers):
    result = high_and_low(numbers)
    assert result == '42 -9', f"Incorrect answer for \"8 3 -5 42 -1 0 0 -9 4 7 4 -4\""


@given(lists(integers(), min_size=1).map(lambda x: ' '.join(map(str, x))))
def test_high_and_low(numbers):
    result = high_and_low(numbers)
    ints = list(map(int, numbers.split(' ')))
    expected_result = f'{max(ints)} {min(ints)}'
    assert result == expected_result, f'Expected "{expected_result}", but got "{result}"'
