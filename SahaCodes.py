string = input('enter for python title: ')
print(string.title())

##############################

str = input("Enter the string")
newstr = ""
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
for i in range(len(str)):
    if str[i] not in vowels:
        newstr = newstr + str[i]
    else:
        newstr = newstr +chr(ord(str[i])+1)

print("Original String:", str)
print("New String:", newstr)

###########################################

string= input("Enter for alternate case")
newstring=""
for c in range(0,len(string)):
  if string[c].islower() :
    newstring = newstring + string[c].upper()
  else:
    newstring = newstring + string[c].lower()
print(newstring)