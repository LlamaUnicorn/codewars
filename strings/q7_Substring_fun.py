# https://www.codewars.com/kata/565b112d09c1adfdd500019c
#
# Complete the function that takes an array of words.
#
# You must concatenate the nth letter from each word to construct a new word which should be returned as a string,
# where n is the position of the word in the list.
#
# For example:
#
# ["yoda", "best", "has"]  -->  "yes"
#   ^        ^        ^
#   n=0     n=1     n=2
# Note: Test cases contain valid input only - i.e. a string array or an empty array; and each word will have enough letters.


# def nth_char(words):
#     result = ''
#     for n, word in enumerate(words):
#         if n < len(word):
#             result += word[n]
#     return result


def nth_char(words):
    return ''.join(w[i] for i, w in enumerate(words))


print(nth_char(['yoda', 'best', 'has']))
