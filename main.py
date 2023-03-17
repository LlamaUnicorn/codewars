# DONE: Get the letter from string
# DONE: Fill the dict_abc with all buttons
# TODO: Split the input into two letters
# TODO: Get the longest letter from string
# TODO: Transform the number to the letter with the maximum value
#         "777777" -->  "sq"` and `"7717777" --> "qs"`
# TODO: 
# TODO: 
# TODO: 


# def translate(str_):
#     # try-catch
#     print("str_:", str_)
#     if str_ in dict_abc:
#         return dict_abc[str_]


# def splitter_(inp):
#     return str(inp)

# dict_abc = {
#     "0": " ",
#     "222": "c",
#     "22": "b",
#     "2": "a",
#     "333": "f",
#     "33": "e",
#     "3": "d",
#     "444": "i",
#     "44": "h",
#     "4": "g",
#     "555": "l",
#     "55": "k",
#     "5": "j",
#     "666": "o",
#     "66": "n",
#     "6": "m",
#     "7777": "s",
#     "777": "r",
#     "77": "q",
#     "7": "p",
#     "888": "v",
#     "88": "u",
#     "8": "t",
#     "9999": "z",
#     "999": "y",
#     "99": "x",
#     "9": "w",
#     }

# test = 888

# splitted = splitter_(test)
# print("splitted:", splitted)
# transformed_text = translate(splitted)
# print("transformed:", transformed_text)




# def phone_words(string_of_nums):
#     keypad = {
#         '2': 'abc',
#         '3': 'def',
#         '4': 'ghi',
#         '5': 'jkl',
#         '6': 'mno',
#         '7': 'pqrs',
#         '8': 'tuv',
#         '9': 'wxyz'
#     }
#     result = ""
#     press_count = 1
#     prev_num = None
#     for i in range(len(string_of_nums)):
#         if string_of_nums[i] == "1":
#             continue
#         elif string_of_nums[i] == "0":
#             result += " "
#             press_count = 1
#             prev_num = None
#             continue
#         elif prev_num != None and string_of_nums[i] == prev_num:
#             press_count += 1
#         else:
#             press_count = 1
#             prev_num = string_of_nums[i]
#         result += keypad[string_of_nums[i]][(press_count-1) % len(keypad[string_of_nums[i]])]
#     return result.lower()


# a = phone_words("443355555566604466690277733099966688")
# print(a)

# def phone_words(string_of_nums):
#     keypad = {
#         '2': 'abc',
#         '3': 'def',
#         '4': 'ghi',
#         '5': 'jkl',
#         '6': 'mno',
#         '7': 'pqrs',
#         '8': 'tuv',
#         '9': 'wxyz'
#     }
#     result = ""
#     press_count = 1
#     prev_num = None
#     for i in range(len(string_of_nums)):
#         if string_of_nums[i] == "1":
#             result += " "
#             press_count = 1
#             prev_num = None
#             continue
#         elif string_of_nums[i] == "0":
#             result += " "
#             press_count = 1
#             prev_num = None
#             continue
#         elif prev_num != None and string_of_nums[i] == prev_num:
#             if string_of_nums[i] != "7" and string_of_nums[i] != "9":
#                 continue
#         else:
#             press_count = 1
#             prev_num = string_of_nums[i]
#         result += keypad[string_of_nums[i]][(press_count-1) % len(keypad[string_of_nums[i]])]
#         press_count += 1
#     return result.lower() if result != "" else ""

# def phone_words(string_of_nums):
#     keypad = {
#         '2': 'abc',
#         '3': 'def',
#         '4': 'ghi',
#         '5': 'jkl',
#         '6': 'mno',
#         '7': 'pqrs',
#         '8': 'tuv',
#         '9': 'wxyz'
#     }
#     result = ""
#     word = ""
#     for i in range(len(string_of_nums)):
#         if string_of_nums[i] == "0":
#             word += " "
#         elif string_of_nums[i] == "1":
#             if i > 0 and string_of_nums[i-1] == "1":
#                 word += "1"
#             else:
#                 word += keypad[string_of_nums[i]][0]
#         elif i > 0 and string_of_nums[i] == string_of_nums[i-1]:
#             if string_of_nums[i] not in ['7', '9'] or len(word) == 0 or word[-1] == '1':
#                 word += keypad[string_of_nums[i]][0]
#             else:
#                 word = word[:-1] + keypad[string_of_nums[i]][0]
#         else:
#             result += word
#             word = keypad[string_of_nums[i]][0]
#     result += word
#     return result.lower()

# def phone_words(string_of_nums):
#     keypad = {
#         '2': 'abc',
#         '3': 'def',
#         '4': 'ghi',
#         '5': 'jkl',
#         '6': 'mno',
#         '7': 'pqrs',
#         '8': 'tuv',
#         '9': 'wxyz'
#     }
#     result = ""
#     word = ""
#     for i in range(len(string_of_nums)):
#         if string_of_nums[i] == "0":
#             word += " "
#         elif string_of_nums[i] == "1":
#             if i > 0 and string_of_nums[i-1] == "1":
#                 word += "1"
#             else:
#                 word += keypad[string_of_nums[i]][0]
#         elif i > 0 and string_of_nums[i] == string_of_nums[i-1]:
#             if string_of_nums[i] not in ['7', '9'] or len(word) == 0 or word[-1] == '1':
#                 word += keypad[string_of_nums[i]][0]
#             else:
#                 word = word[:-1] + keypad[string_of_nums[i]][0]
#         else:
#             result += word
#             word = keypad[string_of_nums[i]][0]
#     result += word
#     return result.lower()

def phone_words(string_of_nums):
    keypad = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    nums = list(string_of_nums)
    result = ""
    current_letter = ""
    count = 0
    for i in range(len(nums)):
        if nums[i] == "0":
            result += " "
            current_letter = ""
            count = 0
        elif i > 0 and nums[i] == nums[i-1]:
            count += 1
            if current_letter != "" and current_letter[-1] == "1":
                current_letter = current_letter[:-1]
            if count > len(keypad[nums[i]])-1:
                count = 0
                current_letter = ""
            else:
                current_letter = keypad[nums[i]][count]
        else:
            if current_letter != "":
                result += current_letter[-1]
            current_letter = keypad[nums[i]][0]
            count = 0
        if count == 1 and current_letter[-1] != "1":
            current_letter += "1"
    result += current_letter
    return result.lower()

a = phone_words("55282")
print(a)


# d = {'apple': 1, 'banana': 2, 'cherry': 3}
# print(list(d.items()))

# print('-' * 10)
# my_keys = ['key1', 'key2', 'key3']
# my_vals = ['1', '2', '3', '4']
# def make_dict(keys, values):
#     result = {}
#     for i, key in enumerate(keys):
#         if i < len(values):
#             result[key] = values[i]
#         else:
#             result[key] = None
#     return result

# my_dict = make_dict(my_keys, my_vals)
# print(my_dict)

# def calculate(num1, num2, op):
#     if op == '+':
#         return num1 + num2
#     elif op == '-':
#         return num1 - num2
#     elif op == '*':
#         return num1 * num2
#     elif op == '/':
#         if num2 == 0:
#             return "Деление на ноль невозможно"
#         else:
#             return num1 / num2
#     else:
#         return "Неизвестная операция"

# result = print(calculate(4, 2, '+'))  # 6
# result = print(calculate(4, 2, '-'))  # 2
# result = print(calculate(4, 2, '*'))  # 8
# result = print(calculate(4, 2, '/'))  # 2
# result = print(calculate(4, 0, '/'))  # "Деление на ноль невозможно"
# result = print(calculate(4, 2, '%'))  # "Неизвестная операция"
