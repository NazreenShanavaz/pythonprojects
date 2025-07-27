def replace_spaces(s):
    result = ""
    for char in s:
        if char == " ":
            result += "_"
        else:
            result += char
    return result

s = input("Enter the string: ")
print(replace_spaces(s))
