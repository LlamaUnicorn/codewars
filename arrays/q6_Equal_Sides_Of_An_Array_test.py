from q6_Equal_Sides_Of_An_Array import find_even_index

test_cases = {
    (): 0,
    (1, -4, 7, 12): 20,
}


def test_find_even_index():
    for names, expected in test_cases.items():
        result = find_even_index(names)
        assert result == expected, f"Incorrect answer for \"{names}\""
