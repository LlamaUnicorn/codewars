# DONE: Get the letter from string
# DONE: Fill the dict_abc with all buttons
# TODO: Split the input into two letters
# TODO: Get the longest letter from string
# TODO: Transform the number to the letter with the maximum value
#         "777777" -->  "sq"` and `"7717777" --> "qs"`
# TODO: 
# TODO: 
# TODO: 


def translate(str_):
    # try-catch
    print("str_:", str_)
    if str_ in dict_abc:
        return dict_abc[str_]


def splitter_(inp):
    return str(inp)

dict_abc = {
    "0": " ",
    "222": "c",
    "22": "b",
    "2": "a",
    "333": "f",
    "33": "e",
    "3": "d",
    "444": "i",
    "44": "h",
    "4": "g",
    "555": "l",
    "55": "k",
    "5": "j",
    "666": "o",
    "66": "n",
    "6": "m",
    "7777": "s",
    "777": "r",
    "77": "q",
    "7": "p",
    "888": "v",
    "88": "u",
    "8": "t",
    "9999": "z",
    "999": "y",
    "99": "x",
    "9": "w",
    }

test = 888

splitted = splitter_(test)
print("splitted:", splitted)
transformed_text = translate(splitted)
print("transformed:", transformed_text)