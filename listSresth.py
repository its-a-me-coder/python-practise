li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
index = 5
li[:] = li[:index]
print(li)

#########################################

li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
index1 = 2
index2 = 7
print(li[index1:index2])

########################################

li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
li.insert(4, 99)
print(li)