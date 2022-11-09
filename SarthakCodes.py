string = input("enter the string to check for the condition")
if any(chr.isdigit() for chr in string) and any(chr.isalpha() for chr in string):
    print("condition is applicable")
else:
    print("condition is not applicable")
################################################################################

string = input("enter the string you want to remove the ith character from")
indx = input("enter the value of i , lower than the length of the string")
if indx > len(string):
    print('invalid')
newstring = ""
for i in range(0,len(string)):
    if i != indx:
        newstring+=string[i]
