from q6_Which_are_in import in_array

test_cases = {
    (tuple(["arp", "live", "strong"]), tuple(["lively", "alive", "harp", "sharp", "armstrong"])): ["arp", "live", "strong"],
    (tuple(["tarp", "mice", "bull"]), tuple(["lively", "alive", "harp", "sharp", "armstrong"])): [],
}


def test_in_array():
    for (list_a, list_b), expected in test_cases.items():
        result = in_array(list(list_a), list(list_b))
        assert result == expected, f"Incorrect answer for \"{list_a, list_b}\""