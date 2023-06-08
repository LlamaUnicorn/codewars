import math


number = int(input())
def square(val):
    return math.sqrt(number)
try:
    square(number)
except ValueError:
    print("It's negative number")

def is_square(n):    
    return False # fix me

