# Complete the square sum function so that it squares each number passed into it and then sums the results together.
# For example, for [1, 2, 2] it should return 9


def square_sum(numbers):
    return sum(num ** 2 for num in numbers)


print(square_sum([1, 2, 2]))