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