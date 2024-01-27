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
vowels = 'aeiouAEIOU'
li = list((char for char in string_ if char not in vowels))
print(li)
