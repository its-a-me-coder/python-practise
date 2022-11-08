string = input()
#doing this without len function
c=0
for i in string:
    c +=1
if c==0:
    print("enter a string with length greater than one,run this again")
else:
    if c%2 ==0:
        print("the string is right")
    else:
        print("sorry the string is wrong")