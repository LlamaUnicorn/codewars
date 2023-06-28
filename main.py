def remove_smallest(numbers):
    if not numbers:
        return []
    min_value = min(numbers)
    min_value_index = numbers.index(min_value)
    return [num for i, num in enumerate(numbers) if i != min_value_index]


numbers = [1,2,3,4,5,1]
print(remove_smallest(numbers))
