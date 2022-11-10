list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 3, 4, 6, 7, 8, 1, 2, 3, 2]
print(list1.count(2))
###############################################

string = "The quick brown fox jumps over the lazy dog"
n = 3
list_new = string.split()
c = 0
for i in list_new:
    if len(i) > n:
        c += 1
print(c)
################################################

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 3, 4, 6, 7, 8, 1, 2, 3, 2]
for i in range(len(list1)):
    try:
        if list1[i] % 2 == 0:
            list1.remove(list1[i])
    except:
        continue
print(list1)
