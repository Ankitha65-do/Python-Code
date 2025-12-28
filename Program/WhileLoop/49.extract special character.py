# .Write a program to extract all the special characters from the given string 

n = input("enter the string : ")
i = 0
while len(n) > i:
    if not n[i].isalnum() and n[i] !=" ":
        print(n[i])
    i += 1


    # isalnum() → checks if character is a letter or number

# not isalnum() → means special character