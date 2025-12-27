#  Write a Program to print all the characters in the string ‘PYTHON’ using while loop. 

string = str(input("enter the string : "))
i = 0
while len(string) > i:
    print(string[i])
    i += 1