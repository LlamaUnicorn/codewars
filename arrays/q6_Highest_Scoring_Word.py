# Given a string of words, you need to find the highest scoring word.
#
# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
#
# For example, the score of abad is 8 (1 + 2 + 1 + 4).
#
# You need to return the highest scoring word as a string.
#
# If two words score the same, return the word that appears earliest in the original string.
#
# All letters will be lowercase and all inputs will be valid.


def high(x):
    # loop over the string and count scores
    # pick and return highest

    letter_scores = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5,
        'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
        'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
        'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
        'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
        'z': 26
    }

    top_word = ''
    max_score = 0
    word_score = 0
    x = x.split()
    for word in x:
        for letter in word:
            word_score += letter_scores[letter]
        if word_score > max_score:
            max_score = word_score
            top_word = word
        word_score = 0

    return top_word


# print(high('man i need a taxi up to ubud'))
print(high('man i need a taxi up to ubud'))


# def high(x):
#     return max(x.split(), key=lambda word: sum(ord(char) - 96 for char in word))
