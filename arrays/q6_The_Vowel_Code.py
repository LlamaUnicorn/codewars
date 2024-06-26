# Step 1: Create a function called encode() to replace all the lowercase vowels in a given string with numbers
#     according to the following pattern:
#
# a -> 1
# e -> 2
# i -> 3
# o -> 4
# u -> 5
# For example, encode("hello") would return "h2ll4". There is no need to worry about uppercase vowels in this kata.
#
# Step 2: Now create a function called decode() to turn the numbers back into vowels according to the same pattern
# shown above.
#
# For example, decode("h3 th2r2") would return "hi there".
#
# For the sake of simplicity, you can assume that any numbers passed into the function will correspond to vowels.


def encode(st):
    replacement = {
        'a': '1',
        'e': '2',
        'i': '3',
        'o': '4',
        'u': '5'
    }
    for char in st:
        if char in replacement:
            st = st.replace(char, replacement[char])

    # st = [replacement[char] for char in st if char in replacement]
    # st = [char for char in ' '.split(st)]
    return st


def decode(st):
    replacement = {
        '1': 'a',
        '2': 'e',
        '3': 'i',
        '4': 'o',
        '5': 'u'
    }
    for char in st:
        if char in replacement:
            st = st.replace(char, replacement[char])
    return st


# def encode(s, t=str.maketrans("aeiou", "12345")):
#     return s.translate(t)
#
#
# def decode(s, t=str.maketrans("12345", "aeiou")):
#     return s.translate(t)


print(encode("hello"))
print(decode("h3 th2r2"))
