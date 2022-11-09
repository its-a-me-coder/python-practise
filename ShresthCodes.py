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
