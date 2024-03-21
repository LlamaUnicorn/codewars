# Implement a pseudo-encryption algorithm which given a string S and an integer N concatenates all the odd-indexed
# characters of S with all the even-indexed characters of S, this process should be repeated N times.
#
# Examples:
#
# encrypt("012345", 1)  =>  "135024"
# encrypt("012345", 2)  =>  "135024"  ->  "304152"
# encrypt("012345", 3)  =>  "135024"  ->  "304152"  ->  "012345"
#
# encrypt("01234", 1)  =>  "13024"
# encrypt("01234", 2)  =>  "13024"  ->  "32104"
# encrypt("01234", 3)  =>  "13024"  ->  "32104"  ->  "20314"
# Together with the encryption function, you should also implement a decryption function which reverses the process.
#
# If the string S is an empty value or the integer N is not positive, return the first argument without changes.

# fails on maximum recursion
# def decrypt(encrypted_text, n):
#     if n == 0 or n < 0 or not encrypted_text:
#         return encrypted_text
#
#     half = len(encrypted_text) // 2
#     odd = encrypted_text[:half]
#     print('odd', odd)
#     even = encrypted_text[half:]
#     print('even', even)
#     combined = list(zip(even, odd))
#     if len(even) > len(odd):
#         combined.append(even[-1])
#     print('combined', combined)
#     flattened = [item for pair in combined for item in pair]
#     encrypted_text = "".join(flattened)
#     print('flattened', encrypted_text)
#     return decrypt(encrypted_text, n - 1)
#
#
# def encrypt(text, n):
#     if n == 0 or n < 0 or not text:
#         return text
#
#     odd = [x for i, x in enumerate(text) if i % 2 != 0]
#     even = [x for i, x in enumerate(text) if i % 2 == 0]
#     result = "".join(odd + even)
#
#     return encrypt(result, n - 1)
def decrypt(encrypted_text, n):
    if n <= 0 or not encrypted_text:
        return encrypted_text

    length = len(encrypted_text)
    for _ in range(n):
        odd = encrypted_text[:length // 2]
        even = encrypted_text[length // 2:]
        encrypted_text = ''.join(i + j for i, j in zip(even, odd + ' '))
    return encrypted_text.strip()


def encrypt(text, n):
    if n <= 0 or not text:
        return text

    for _ in range(n):
        text = text[1::2] + text[::2]
    return text


# print(encrypt('JK>~~pyb#}iI{T_AR_', 993))

# print(decrypt("hsi  etTi sats!", 1))
# print(decrypt("s eT ashi tist!", 2))
print(decrypt("135024!", 1))
# print(decrypt("304152", 2))
# print(encrypt("012345", 1))
# print(encrypt("012345", 2))
