# Write a program to get the following output 
    #    input=’abcd’ 
    #    output={‘a’:97,’b’:98,’c’:99,’d’:100} 

s = input("enter the string : ")
i = 0

while len(s) > i :
    print(s[i] , ":", ord(s[i]))
    i += 1
    