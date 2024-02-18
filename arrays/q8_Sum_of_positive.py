def positive_sum(arr):
    return sum([num for num in arr if num > 0]) if arr else 0


print(positive_sum([1, -4, 7, 12]))
