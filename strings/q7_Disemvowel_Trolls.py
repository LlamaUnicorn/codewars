# https://www.codewars.com/kata/52fba66badcd10859f00097e
#
# Trolls are attacking your comment section!
#
# A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.
#
# Your task is to write a function that takes a string and return a new string with all vowels removed.
#
# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
#
# Note: for this kata y isn't considered a vowel.

# def disemvowel(string_):
#     vowels = 'aeiouAEIOU'
#     for i, char in enumerate(string_):
#         if char in vowels:
#             string_ = string_.replace(char, '')
#     return string_


def disemvowel(string_):
    vowels = 'aeiouAEIOU'
    return ''.join(char for char in string_ if char not in vowels)


print(disemvowel('You should leave'))

string_ = 'You should leave'
vowels_ = 'aeiouAEIOU'
li = list((char for char in string_ if char not in vowels_))
print(li)
