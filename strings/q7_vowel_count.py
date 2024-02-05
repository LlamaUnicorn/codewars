def get_count(sentence):
    vowels = 'aeiou'
    vowels_count = 0
    for letter in sentence:
        if letter in vowels:
            vowels_count += 1
    return vowels_count


def get_count_2(sentence):
    vowels = 'aeiou'
    filtered_vowels = filter(lambda letter: letter in vowels, sentence)
    # filtered_vowels = list(filter(lambda letter: letter in vowels, sentence))
    # print(filtered_vowels)
    vowels_count = sum(map(lambda vowel: 1, filtered_vowels))
    return vowels_count


print(get_count_2('yoda'))
