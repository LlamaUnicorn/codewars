# Complete the solution so that it reverses the string passed into it.

# 'world'  =>  'dlrow'
# 'word'   =>  'drow'

# https://www.codewars.com/kata/5168bb5dfe9a00b126000018/train/python

# My convoluted solution
def solution(string):
    plist = list(string)
    reversed = plist[::-1]
    return "".join(reversed)


# Solution
# def solution(str):
#   return str[::-1]