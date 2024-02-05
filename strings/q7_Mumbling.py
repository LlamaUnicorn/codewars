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
