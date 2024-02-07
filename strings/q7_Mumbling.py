# The examples below show you how to write function accum:
#
# Examples:
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"
# The parameter of accum is a string which includes only letters from a..z and A..Z.


# def accum(st):
#     result = ''
#     for i, char in enumerate(st, 1):
#         result += (char * i).capitalize()
#         if 1 < len(st) != i:
#             result += '-'
#     return result


def accum(st):
    return '-'.join((a * i).title() for i, a in enumerate(st, 1))


print(accum('cwAt'))
