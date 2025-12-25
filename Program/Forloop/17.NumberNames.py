#  Write a program to display the number names of the digits of a number entered by 
# user, for example if the number is 231 then output should be Two Three One 

n = input("Enter the Number : ")
for i in n:
    if i == '0':
        print("Zero",end = " ")
    elif i == '1':
        print("One",end = " ")
    elif i == '2':
        print("Two",end = " ")
    elif i == '3':
        print("Three",end = " ")
    elif i == '4':
        print("Four",end = " ")
    elif i == '5':
        print("Five",end = " ")
    elif i == '6':
        print("Six",end = " ")
    elif i == '7':
        print("Seven",end = " ")
    elif i == '8':
        print("Eight",end = " ")
    elif i == '9':
        print("Nine",end = " ")
