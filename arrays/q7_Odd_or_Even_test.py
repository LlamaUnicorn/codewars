from q7_Odd_or_Even import odd_or_even

test_cases = {
    (0, 1, 4): 'odd',
    (0, -1, -5): 'even',
}


def test_odd_or_even():
    for names, expected in test_cases.items():
        result = odd_or_even(names)
        assert result == expected, f"Incorrect answer for \"{names}\""