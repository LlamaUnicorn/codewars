def high_and_low(numbers):
    ints = [int(i) for i in numbers.split(' ')]
    max_int = max(ints)
    min_int = min(ints)

    return f'{max_int} {min_int}'


print(high_and_low('1 2 3'))
