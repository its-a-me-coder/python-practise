string = input("Enter a word to eliminate same case letters")
nono = []
final =""
for i in string:
    if i not in nono:
        final+=i
        nono.append(i)
print(final)

#################################################################

string = input("enter a sentence to exchange commas and spaces with each other")
string1=[]
for i in string:
    if i == ' ':
        string1+=','
    elif i == ',':
        string1+=' '
    else:
        string1+=i
print(''.join(string1))