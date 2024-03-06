# You will be given an array of numbers. You have to sort the odd numbers in ascending order
# while leaving the even numbers at their original positions.
#
# Examples
# [7, 1]  =>  [1, 7]
# [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]


def sort_array(source_array):
    # DONE get odd ones
    # DONE sort odd ones
    # DONE return sorted at the spaces where they were

    odd_index = []
    odd_nums = []

    for i, num in enumerate(source_array):
        if num % 2 != 0:
            odd_index.append(i)
            odd_nums.append(num)

    odd_nums = sorted(odd_nums)

    odd_index.sort(reverse=True)
    for i in odd_index:
        source_array.pop(i)
    odd_index.sort(reverse=True)

    odd_index.sort(reverse=False)
    for i in odd_index:
        for num in odd_nums:
            source_array.insert(i, num)
            odd_nums.remove(num)
            break
    return source_array


print(sort_array([5, 8, 6, 3, 4]))


# def sort_array(arr):
#     odds = sorted((x for x in arr if x % 2 != 0), reverse=True)
#     return [x if x % 2 == 0 else odds.pop() for x in arr]
