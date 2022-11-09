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
string = input('enter for most repeated: ') #making a dictionary with key mein element and value mein frequency
dict1 = {}
for i in string:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1

repeated_often = max(dict1, key=dict1.get) #instead of using count now we are only comparing the values of the keys
print("the character is", repeated_often)