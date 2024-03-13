from q6_Two_Sum import two_sum


def test_two_sum():
    assert (a := two_sum([1, 2, 3], 4)) == (0, 2) or a == (2, 0), a
    assert (a := two_sum([3, 2, 4], 6)) == (1, 2) or a == (2, 1), a
    print("All tests passed.")
