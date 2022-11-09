string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
if string1 == string2:
    print("Yes")

else:
    print("No")
#############################################
str1 = input("Please enter the string for the vowels and consonants check: ")
vowels = 0
consonants = 0

for i in str1:
    if i.isalnum():
        if i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            vowels = vowels + 1
        else:
            consonants = consonants + 1

print("Number of Vowels = ", vowels)
print("Number of Consonants = ",
      consonants)  # but this is wrong should i use regex??, but that requires external library

##########################################

string1 = input("enter the superset string S  :")
string2 = input("enter the string T, to check if its a subset of the superset  :")

if string1.find(string2) != -1:
    print("it is in the string")
else:
    print("not in S")


