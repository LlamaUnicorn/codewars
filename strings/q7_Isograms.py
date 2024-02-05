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
