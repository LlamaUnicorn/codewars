# import string
# from hypothesis.strategies import just, text, lists, integers
#
# from hypothesis import given, example, strategies as st
#
# from q6_Create_Phone_Number import create_phone_number


# test_cases = {
#     ("1, 2, 3, 4, 5, 6, 7, 8, 9, 0"): '(123) 456-7890',
# }
#
#
# @given(just(['1, 2, 3, 4, 5, 6, 7, 8, 9, 0']))
# def test_create_phone_number_example(word):
#     result = create_phone_number(word)
#     assert result == '(123) 456-7890', f"Incorrect answer for \"{word}\""
