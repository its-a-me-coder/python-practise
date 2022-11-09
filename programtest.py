#user input , 1,2,3, if user inputs 1 -> take string ,return same string
#if 2 -> take string, reverse string
#if 3 -> vowels print only
choice = 0
while choice!=4 :
    choice= int(input("enter the choice 1,2,3 :"))
    if choice == 1:
        string = input(" enter the string here")
        print("the result is",string)
        choice = int(input("enter the choice 1,2,3,4 :"))
    if choice == 2:
        string = input(" enter the string here")
        print("the result is",string[::-1])
        choice = int(input("enter the choice 1,2,3,4 :"))
    if choice == 3:
        ls = ['a','e','i','o','u']
        str = ""
        string = input(" enter the string here")
        for i in string:
            if i in ls:
                str += i+","
        print (str)
        choice = int(input("enter the choice 1,2,3,4 :"))

