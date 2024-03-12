from q6_The_Supermarket_Queue import queue_time

test_cases = {
    (tuple([5, 3, 4]), 1): 12,
    (tuple([10, 2, 3, 3]), 2): 10,
}


def test_queue_time():
    for (list_a, list_b), expected in test_cases.items():
        result = queue_time(list(list_a), list_b)
        assert result == expected, f"Incorrect answer for \"{list_a, list_b}\""
