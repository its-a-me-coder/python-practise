val = int(input('Enter any number for palindrome: '))
if str(val) == str(val)[::-1]:
    print('PALINDROME')
else:
    print('NOPE')

#############################

string = input('enter for duplicate: ')
dups = []
for ch in string:
    if string.count(ch) > 1 and ch not in dups:
        dups.append(ch)
print(dups)
#############################
string1 = input('enter for least: ')
lst = list(string1)

print((min(string1, key=string1.count)))

###################################
string = input('enter for least repeated: ')
dict1 = {}  # making a dictionary with key mein element and value mein frequency
for i in string:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1
least_often = []
current = -1
for i in range(0, len(dict1)):
    x = min(dict1, key=dict1.get)
    if current == int(dict1.get(x)) or current == -1:
        least_often.append(x)
        current = dict1.get(x)
        dict1.pop(x)
print("the character(s) is/are: ", ', '.join(least_often))
