def nth_char(words):
    result = ''
    for n, word in enumerate(words):
        if n < len(word):
            result += word[n]
    return result


print(nth_char(['yoda', 'best', 'has']))
