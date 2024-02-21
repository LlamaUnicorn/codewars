from hypothesis import given, strategies as st

from q7_Sum_of_two_lowest_positive_integers import sum_two_smallest_numbers

test_cases = {
    (19, 5, 42, 2, 77): 7,
    (10, 343445353, 3453445, 3453545353453): 3453455,
}


def test_sum_two_smallest_numbers_example():
    for names, expected in test_cases.items():
        result = sum_two_smallest_numbers(list(names))
        assert result == expected
