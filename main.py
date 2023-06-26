from copy import deepcopy

def remove_smallest(numbers):
    new_numbers = deepcopy(numbers)
    return new_numbers.remove(min(new_numbers))


numbers = [1,2,3,4,5]
print(remove_smallest(numbers))
