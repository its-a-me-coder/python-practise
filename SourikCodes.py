string = input("Enter a word to eliminate same case letters")
final = ""
for i in string:
    if i not in final:
        final += i
print(final)

#################################################################

string = input("enter a sentence to exchange commas and spaces with each other")
string1 = ""
for i in string:
    if i == ' ':
        string1 += ','
    elif i == ',':
        string1 += ' '
    else:
        string1 += i
print(''.join(string1))

#################################################################

string1 = input('enter for most repeated: ')
lst = list(string1)
print((max(string1, key=string1.count)))
################################################################
string = input('enter for most repeated: ')  # making a dictionary with key mein element and value mein frequency
dict1 = {}
for i in string:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1
repeated_often = []
current = -1
for i in range(0, len(dict1)):
    x = max(dict1, key=dict1.get)
    if current == int(dict1.get(x)) or current == -1:
        repeated_often.append(x)
        current = dict1.get(x)
        dict1.pop(x)
print("the character(s) is/are: ", ', '.join(repeated_often))
