string = input('enter the string to capitalize letters')
string1 = string.title()
ls = string1.split(" ")
x = []
for i in ls:
    x.append(i[0:-1] + i[-1].upper())
print(' '.join(x))

########################################################
string = "SouriksssDuttaSSS"
x = string[0].lower()
y = string[0].upper()
string2 = (string[1:].replace(x, '$'))
print(string[0]+string2)
string3 = (string[0] + (string2.replace(y, '$')))
print(string3)
########################################################
string = input("enter the string:  ")
if len(string) > 1:
    newstr = ""
    newstr = string[0] + string[1] + string[-2] + string[-1]
    print(newstr)
else:
    print("empty string")
