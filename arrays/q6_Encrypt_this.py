# Encrypt this!
#
# You want to create secret messages which can be deciphered by the Decipher this! kata. Here are the conditions:
#
# Your message is a string containing space separated words.
# You need to encrypt each word in the message using the following rules:
# The first letter must be converted to its ASCII code.
# The second letter must be switched with the last letter
# Keepin' it simple: There are no special characters in the input.
# Examples:
# encrypt_this("Hello") == "72olle"
# encrypt_this("good") == "103doo"
# encrypt_this("hello world") == "104olle 119drlo"


def encrypt_this(text):
    text = text.split()
    result = ''
    for char in text:
        result += str(ord(char[0])) + (char[-1] + char[2:-1] + char[1] if len(char) > 2 else char[1:])
        result += ' '
    return result.strip()


# return ' '.join([str(ord(word[0])) + (word[-1] + word[2:-1] + word[1] if len(word) > 2 else word[1:]) for word in text.split()])

# print(encrypt_this("Hello"))  # "72olle"
# print(encrypt_this("hello world"))  # "104olle 119drlo"
print(encrypt_this("A wise old owl lived in an oak"))  # "65 119esi 111dl 111lw 108dvei 105n ::n 111ka"
