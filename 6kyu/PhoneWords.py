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
    for i, num in enumerate(nums):
        if num == "1":
            result += current_letter
            count = 0
            current_letter = ""
        elif num == "0":
            result += current_letter + " "
            current_letter = ""
            count = 0
        elif i > 0 and num == nums[i-1]:
            count += 1
            if count > len(keypad[num])-1:
                count = 0
                result += current_letter
            if current_letter != "" and current_letter[-1] == "1":
                current_letter = current_letter[:-1]
            else:
                current_letter = keypad[num][count]
        else:
            if current_letter != "":
                result += current_letter[-1]
            current_letter = keypad[num][0]
            count = 0
    result += current_letter
    return result.lower()

a = phone_words("55282")
print(a)