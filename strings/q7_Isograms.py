# An isogram is a word that has no repeating letters, consecutive or non-consecutive.
# Implement a function that determines whether a string that contains only letters is an isogram.
# Assume the empty string is an isogram. Ignore letter case.
#
# Example: (Input --> Output)
#
# "Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)
#
# isIsogram "Dermatoglyphics" = true
# isIsogram "moose" = false
# isIsogram "aba" = false


# def is_isogram(string):
#     if string == '': return True
#     letters = list()
#     for letter in string:
#         if letter == letter.lower(): return False
#         elif letter.lower() not in letters:
#             letters.append(letter)
#         else:
#             return False
#
#     return True

def is_isogram(string):
    string = string.lower()
    return len(string) == len(set(string))


print(is_isogram('Aa'))
