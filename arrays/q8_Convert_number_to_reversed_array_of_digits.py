# Convert number to reversed array of digits
# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.
#
# Example(Input => Output):
# 35231 => [1,3,2,5,3]
# 0 => [0]


# def digitize(n):
#     n = str(n)
#     return [int(x) for x in n[::-1]]
def digitize(n):
    reversed_digits = []
    while n > 0:
        reversed_digits.append(n % 10)
        n = n // 10
    return reversed_digits if reversed_digits else [0]


print(digitize(35231))
