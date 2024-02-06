def to_jaden_case(string):
    split_and_capitalize = [word.capitalize() for word in string.split()]
    joined_string = " ".join(split_and_capitalize)
    return joined_string


quote = "How can mirrors be real if our eyes aren't real"

print(to_jaden_case(quote))
