from q6_Take_a_Ten_Minutes_Walk import is_valid_walk

test_cases = {
    ('n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's'): True,
}


def test_is_valid_walk():
    for names, expected in test_cases.items():
        result = is_valid_walk(names)
        assert result == expected, f"Incorrect answer for \"{names}\""
