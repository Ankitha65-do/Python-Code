# Write a program to extract all the upper case character ,lower case 
# character ,numbers and special characters into four different output variables 
# from the given string 

s = input("enter the string : ")
i = 0
upper = ""
lower = ""
number = ""
special = ""
while len(s) > i :
    if s[i].isupper():
        upper += s[i]
    elif s[i].islower():
        lower += s[i]
    elif s[i].isdigit():
        number +=s[i]
    else :
        special += s[i]
    i += 1
print("Upper Case are : ", upper)
print("lower case are : ", lower)
print("numbers are : ",number)
print("special character are : ", special)
   