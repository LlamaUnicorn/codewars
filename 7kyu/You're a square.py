import math

def is_square(n):    
    if n < 0:
        return False
    sqrt_num = math.sqrt(n)
    return sqrt_num.is_integer()

# solutions

# import math
# def is_square(n):
#     return n > -1 and math.sqrt(n) % 1 == 0;

