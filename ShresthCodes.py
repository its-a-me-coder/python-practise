val = int(input('Enter any number for palindrome: '))
if str(val) == str(val)[::-1]:
    print('PALINDROME')
else:
    print('NOPE')

#############################

string = input('enter for duplicate: ')
dups=[]
for ch in string:
  if string.count(ch)>1 and ch not in dups:
    dups.append(ch)
print(dups)
#############################
string1 = input('enter for least: ')
lst = list(string1)

print((min(string1, key=string1.count)))

###################################
string = input('enter for least repeated: ')
dict1 = {}  #making a dictionary with key mein element and value mein frequency
for i in string:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1

least_often = min(dict1, key=dict1.get)  #instead of using count now we are only comparing the values of the keys
print("the character is", least_often)
