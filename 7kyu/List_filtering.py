def filter_list(l):
    'return a new list with the strings filtered out'
    return [i for i in l if not isinstance(i, str)]
    # return [i for i in l if type(i) == int]
    # return [i for i in l if isinstance(i, int)]


l = [1, 2, 'a', 'b']
filter_list(l)
print(filter_list(l))