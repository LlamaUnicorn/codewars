from q7_Ones_and_Zeros import binary_array_to_number

test_cases = {
    (0, 0, 0, 1): 1,
    (0, 0, 1, 0): 2,
    (0, 1, 0, 1): 5,
    (1, 0, 0, 1): 9,
    (0, 1, 1, 0): 6,
    (1, 1, 1, 1): 15,
    (1, 0, 1, 1): 11,
}


def test_binary_array_to_number():
    for names, expected in test_cases.items():
        result = binary_array_to_number(names)
        assert result == expected, f"Incorrect answer for \"{names}\""
