def max_diff(lst):
    if len(lst) <= 1:
        return 0

    max_value, min_value = max(lst), min(lst)
    return max_value - min_value

# def max_diff(list):
#     return max(list) - min(list) if list else 0