numbers = [5, 10, 15, 20, 25, 30, 35]
print([numbers[i] for i in range((len(numbers) - 1), -1, -1)])
##########################################################

string = " and awdneg and awdasdawand"
subString = "and"
c = 0
for i in range(len(string)):
    currentSubString = ""
    for j in range(i, len(string)):
        currentSubString += string[j]
        if currentSubString == subString:
            c += 1
print(c)

############################################################
list_multiply = [1, 2, 3, 4, 5, 6, 7]
list_multiplied = map(lambda i: i * 5, list_multiply)
print(list(list_multiplied))
print(type(list_multiplied))
