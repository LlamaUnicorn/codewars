def filter_list(l):
    print(f'{l=}')
    'return a new list with the strings filtered out'
    for i in l:
        print(f'{i=}')
        if type(i) != int:
            print(i)
            l.remove(i)
    print(f'{l=}')
    return l