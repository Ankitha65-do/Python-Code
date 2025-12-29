# Write a program to get the following output 
    #    input=’hello’ 
    #    output={0:’h’ , 1:’e’ , 2:’l’ , 3:’l’ , 4:’o’}


s = input("enter the string : ")
i = 0
result = {}
while len(s) > i :
    result[i] = s[i]
    i += 1

print(result)