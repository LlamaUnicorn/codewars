def get_count(sentence):
    vowels = 'aeiou'
    vowels_count = 0
    for letter in sentence:
        if letter in vowels:
            vowels_count += 1
    return vowels_count