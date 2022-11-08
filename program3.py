string = "python is a good language"
c = 0
for i in string:
    if i == " ":
        c += 1

print(c)
print(string.count(" "))