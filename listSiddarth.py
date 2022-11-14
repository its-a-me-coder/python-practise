########################################
string = ""
list1 = [1, 2, 3]
list2 = [5, 6, 7, 9, 11]
for i in range(0, max(len(list1), len(list2))):
    try:
        string += str(list1[i])
        string += str(list2[i])
    except:
        if len(list1) > len(list2):
            string += str(list1[i])
        else:
            string += str(list2[i])
print(string)
#########################################

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 3, 4, 6, 7, 8, 1, 2, 3, 2]
n = 4  # any number given by the user
list_1[:] = list_1[-n:] + list_1[:-n]
print(list_1)
###########################################

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 3, 4, 6, 7, 8, 1, 2, 3, 2]
n = 4  # any number given by the user
i = 0
for i in range(n):
    print(list_1[-1])
    first_ele = list_1[len(list_1) - 1]
    list_1[i] = first_ele
    for j in range(len(list_1) - 1, i, -1):
        list_1[j] = list_1[j - 1]
print(list_1)
