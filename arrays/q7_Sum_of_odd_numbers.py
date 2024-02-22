# Given the triangle of consecutive odd numbers:
#
#              1
#           3     5
#        7     9    11
#    13    15    17    19
# 21    23    25    27    29
# ...
# Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)
#
# 1 -->  1
# 2 --> 3 + 5 = 8
# 27
# 64

# Pattern Recognition: The first step in problems like these is to look for a pattern.
# You’ve already been given the sums of the first two rows. Try calculating the sums of the next few rows and see if you can spot a pattern.

# Mathematical Representation: Once you’ve spotted a pattern, the next step is to represent it mathematically.
# This often involves figuring out a formula that describes the pattern you’ve observed.

# Proof: After you’ve come up with a mathematical representation of the pattern, you should try to prove it.
# This step ensures that the pattern you’ve observed holds for all cases and is not just a coincidence.

# Implementation: Finally, once you’ve proven your formula, you can implement it in code to calculate
# the sum of the nth row.


def row_sum_odd_numbers(n):
    return n ** 3


print(row_sum_odd_numbers(2))
