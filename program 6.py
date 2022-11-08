string = "python is a good language"
ls1 = []
ls2 = []
for i in range(0,len(string)):
    if i%2 == 0:
        ls1.append(string[i])
    else:
        ls2.append(string[i])
#mixed i can choose to change it to string or keep it like that
print("Even Characters:", string[::2],ls1)
print("Odd Characters:", string[1::2],ls2)