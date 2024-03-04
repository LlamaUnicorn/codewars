from q6_Tribonacci_Sequence import tribonacci

test_cases = {
    (tuple([1, 1, 1]), 10): [1, 1, 1, 3, 5, 9, 17, 31, 57, 105],
    (tuple([0, 0, 1]), 10): [0, 0, 1, 1, 2, 4, 7, 13, 24, 44],
    (tuple([0, 0, 0]), 10): [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
}


def test_tribonacci():
    for (list_a, len), expected in test_cases.items():
        result = tribonacci(list(list_a), len)
        assert result == expected, f"Incorrect answer for \"{list_a, len}\""
