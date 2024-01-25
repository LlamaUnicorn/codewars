# def nth_char(words):
#     result = ''
#     for n, word in enumerate(words):
#         if n < len(word):
#             result += word[n]
#     return result


def nth_char(words):
    return ''.join(w[i] for i, w in enumerate(words))


print(nth_char(['yoda', 'best', 'has']))
