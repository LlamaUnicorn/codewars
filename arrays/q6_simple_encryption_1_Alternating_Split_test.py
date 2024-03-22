from q6_simple_encryption_1_Alternating_Split import decrypt, encrypt

# test_cases = {
#     (tuple([1, 2]), tuple([1])): [2],
#     (tuple([1, 2, 2, 2, 3]), tuple([2])): [1, 3],
#     (tuple("hsi  etTi sats!"), tuple([1])): "This is a test!",
#     (tuple("s eT ashi tist!"), tuple([2])): "This is a test!",
#     (tuple("JK>~~pyb#}iI{T_AR_"), tuple([993])): "This is a test!",
# }
#
#
# def test_decrypt():
#     for (list_a, list_b), expected in test_cases.items():
#         result = decrypt(list(list_a), int(list_b))
#         assert result == expected, f"Incorrect answer for \"{list_a, list_b}\""

test_cases = {
    ("012345", 1): "135024",
    ("012345", 2): "304152",
    ("012345", 3): "012345",
    ("01234", 1): "13024",
    ("01234", 2): "32104",
    ("01234", 3): "20314",
}

def test_decrypt():
    for (text, n), expected in test_cases.items():
        encrypted_text = encrypt(text, n)
        result = decrypt(encrypted_text, n)
        assert result == text, f"Incorrect answer for \"{text, n}\""

        result = encrypt(text, n)
        assert result == expected, f"Incorrect answer for \"{text, n}\""


test_decrypt()
