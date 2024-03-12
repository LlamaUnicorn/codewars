from q6_array_diff import array_diff

test_cases = {
    (tuple([1, 2]), tuple([1])): [2],
    (tuple([1, 2, 2, 2, 3]), tuple([2])): [1, 3],
}


def test_array_diff():
    for (list_a, list_b), expected in test_cases.items():
        result = array_diff(list(list_a), list(list_b))
        assert result == expected, f"Incorrect answer for \"{list_a, list_b}\""
