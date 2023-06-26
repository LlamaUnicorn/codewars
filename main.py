def remove_smallest(numbers):
    new_numbers = numbers.copy()
    return new_numbers.remove(min(numbers))


numbers = [1,2,3,4,5]
print(remove_smallest(numbers))
