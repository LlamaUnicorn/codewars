from q8_Sum_of_positive import positive_sum

test_cases = {
    (): 0,
    (1, -4, 7, 12): 20,
}


def test_positive_sum():
    for names, expected in test_cases.items():
        result = positive_sum(names)
        assert result == expected, f"Incorrect answer for \"{names}\""
