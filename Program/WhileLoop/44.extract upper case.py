# .Write a program to extract all the upper case character from the given string 
# s=input(‘enter the string:’)

s = str(input("enter the string : "))
i = 0
while len(s) > i:
    if s[i].isupper() :
        print(s[i])
    i += 1