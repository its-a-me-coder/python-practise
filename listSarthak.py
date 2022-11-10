list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 3, 4, 6, 7, 8, 1, 2, 3, 2]
list_new = []
for i in list1:
    if i not in list_new:
        list_new.append(i)
print(list_new)
##################################################################

string = "The quick brown fox jumps over the lazy dog"
n = "t"
res = ""
new_string = string.split()
for i in new_string:
    if i[0].lower() == n:
        res+=("  -->"+ i )
print(res)