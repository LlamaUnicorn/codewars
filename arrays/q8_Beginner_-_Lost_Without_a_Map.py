# Given an array of integers, return a new array with each value doubled.
#
# For example:
#
# [1, 2, 3] --> [2, 4, 6]


def maps(a):
    return [x * 2 for x in a]


print(maps([1, 2, 3]))
