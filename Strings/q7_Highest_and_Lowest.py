def high_and_low(numbers):
    ints = numbers.replace(' ', ', ')
    ints_list = list(numbers)
    # print(numbers)
    print(ints)
    print(ints_list)
    # ints = map(int, ints_list)
    max_int = max(numbers)
    min_int = min(numbers)
    print(max_int)
    print(min_int)

    return f'{max_int} {min_int}'


print(high_and_low('1 2 3'))
