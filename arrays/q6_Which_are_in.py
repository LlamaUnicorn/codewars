# Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order of the strings
# of a1 which are substrings of strings of a2.
#
# Example 1:
# a1 = ["arp", "live", "strong"]
#
# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
#
# returns ["arp", "live", "strong"]
#
# Example 2:
# a1 = ["tarp", "mice", "bull"]
#
# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
#
# returns []
#
# Notes:
# Arrays are written in "general" notation. See "Your Test Cases" for examples in your language.
# In Shell bash a1 and a2 are strings. The return is a string where words are separated by commas.
# Beware: In some languages r must be without duplicates.


def in_array(array1, array2):
    result = []
    for part in array1:
        for word in array2:
            if part in word:
                result.append(part)
    return list(sorted(set(result)))


print(in_array(["arp", "live", "strong"], ["lively", "alive", "harp", "sharp", "armstrong"]))


# return sorted(set([word for word in array1 for word_2 in array2 if word in word_2]))


# def in_array(a1, a2):
#     return sorted(set(s1 for s1 in a1 if any(s1 in s2 for s2 in a2)))
