# Count the number of Duplicates
# Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits
# that occur more than once in the input string. The input string can be assumed to contain only alphabets
# (both uppercase and lowercase) and numeric digits.
#
# Example
# "abcde" -> 0 # no characters repeats more than once
# "aabbcde" -> 2 # 'a' and 'b'
# "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
# "indivisibility" -> 1 # 'i' occurs six times
# "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
# "aA11" -> 2 # 'a' and '1'
# "ABBA" -> 2 # 'A' and 'B' each occur twice


def duplicate_count(text):
    result = 0
    text = text.lower()
    counting_dict = dict()
    for char in text:
        if char not in counting_dict:
            counting_dict[char] = 1
        else:
            counting_dict[char] += 1
    for k, v in counting_dict.items():
        if v > 1:
            result += 1
    # for char in text:
    #     if text.count(char) > 1:
    #         result += 1
    #         text = text.replace(char, '')
    return result


print(duplicate_count('aabBcde'))


# def duplicate_count(text):
#     text = text.lower()
#     counting_dict = {char: text.count(char) for char in text}
#     return sum(1 for v in counting_dict.values() if v > 1)
