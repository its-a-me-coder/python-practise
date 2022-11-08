string = "python is a good language"
result_string = ''
for char in string:
    if ord(char) >= 65:  # only checking if in lower case
        result_string += chr(ord(char) - 32)
    if char == " ":
        result_string += " "
print(result_string)
