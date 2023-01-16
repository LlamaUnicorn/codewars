# TODO: Get the letter from string
# TODO: Get the longest letter from string
# TODO: Transform the number to the letter with the maximum value
#         "777777" -->  "sq"` and `"7717777" --> "qs"`
# TODO: 
# TODO: 
# TODO: 


def translate(str_):
    # try-catch
    print('str_:', str_)
    if str_ in dict_abc:
        return dict_abc[str_]


def splitter_(inp):
    return str(inp)

dict_abc = {'222': "c",
          '22': "b",
          '2': "a",
          '333': "f",
          '33': "e",
          '3': "d",
          '7777': 's',
          '777': 'r',
          '77': 'q',
          '7': 'p'
         }

test = 7777

splitted = splitter_(test)
print('splitted:', splitted)
transformed_text = translate(splitted)
print('transformed:', transformed_text)