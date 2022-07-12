def approx_equals(a, b):
    result = (abs(a-b)) <= 0.001
    return result

# Best Practice
# def approx_equals(a, b):
#     return abs(a-b) < 0.001


#
# from math import isclose
#
# def approx_equals(a, b):
#     return isclose(a, b, rel_tol=0, abs_tol=1e-3)