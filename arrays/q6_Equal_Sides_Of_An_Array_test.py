from q6_Equal_Sides_Of_An_Array import find_even_index

test_cases = {
    (1, 2, 3, 4, 3, 2, 1): 3,
    (1, 100, 50, -51, 1, 1): 1,
    (20, 10, -80, 10, 10, 15, 35): 0,
}


def test_find_even_index():
    for names, expected in test_cases.items():
        result = find_even_index(names)
        assert result == expected, f"Incorrect answer for \"{names}\""
