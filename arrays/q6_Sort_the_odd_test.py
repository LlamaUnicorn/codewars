from q6_Sort_the_odd import sort_array

test_cases = {
    (5, 8, 6, 3, 4): (3, 8, 6, 5, 4),
    (7, 1): (1, 7),
    (9, 8, 7, 6, 5, 4, 3, 2, 1, 0): (1, 8, 3, 6, 5, 4, 7, 2, 9, 0),
}


def test_sort_array():
    for names, expected in test_cases.items():
        result = sort_array(list(names))
        assert result == list(expected), f"Incorrect answer for \"{names}\""
