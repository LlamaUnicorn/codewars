def remove_smallest(numbers):
    removed_minimum = [
        i for i in numbers
        if i > min(numbers)
    ]
    return [] if numbers == [] else removed_minimum


numbers = [1,2,3,4,5]
print(remove_smallest(numbers))
