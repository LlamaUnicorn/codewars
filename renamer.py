def normalize_file_name(string):
    modified_string = string.replace(" ", "_")
    modified_string = modified_string.replace(",", "")
    modified_string = modified_string.replace("/", "")
    modified_string = modified_string.replace("\\", "")
    modified_string = modified_string.replace("%", "")
    modified_string = modified_string.lower()
    return modified_string


my_string = "Head, Tail, Init and Last"
modified_string = normalize_file_name(my_string)
print(modified_string)
