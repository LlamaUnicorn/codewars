from q6_simple_encryption_1_Alternating_Split import decrypt

test_cases = {
    (tuple([1, 2]), tuple([1])): [2],
    (tuple([1, 2, 2, 2, 3]), tuple([2])): [1, 3],
    (tuple("hsi  etTi sats!"), tuple([1])): "This is a test!",
    (tuple("s eT ashi tist!"), tuple([2])): "This is a test!",
    (tuple("JK>~~pyb#}iI{T_AR_"), tuple([993])): "This is a test!",
}


def test_decrypt():
    for (list_a, list_b), expected in test_cases.items():
        result = decrypt(list(list_a), list(list_b))
        assert result == expected, f"Incorrect answer for \"{list_a, list_b}\""
