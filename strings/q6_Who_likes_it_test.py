from q6_Who_likes_it import likes


# def likes(names):
#     match names:
#         case []:
#             return 'no one likes this'
#         case [name]:
#             return f'{name} likes this'
#         case [name1, name2]:
#             return f'{name1} and {name2} like this'
#         case [name1, name2, name3]:
#             return f'{name1}, {name2} and {name3} like this'
#         case _:
#             return 'error'


test_cases = {
    (): "no one likes this",
    ("Peter",): "Peter likes this",
    ("Jacob", "Alex"): "Jacob and Alex like this",
    ("Max", "John", "Mark"): "Max, John and Mark like this",
    ("Alex", "Jacob", "Mark", "Max"): "Alex, Jacob and 2 others like this",
}


def test_likes():
    for names, expected in test_cases.items():
        result = likes(names)
        assert result == expected, f"Incorrect answer for \"{names}\""
