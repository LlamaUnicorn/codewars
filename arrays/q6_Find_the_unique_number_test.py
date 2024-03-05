from q6_Find_the_unique_number import find_uniq

test_cases = {
    (1, 1, 1, 2, 1, 1): 2,
    (0, 0, 0.55, 0, 0): 0.55,
}


def test_find_uniq():
    for names, expected in test_cases.items():
        result = find_uniq(names)
        assert result == expected, f"Incorrect answer for \"{names}\""