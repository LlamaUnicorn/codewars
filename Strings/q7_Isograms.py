def is_isogram(string):
    if string == '': return True
    letters = list()
    for letter in string:
        if letter.lower() not in letters:
            letters.append(letter)
        else:
            return False

    return True


print(is_isogram('moose'))
