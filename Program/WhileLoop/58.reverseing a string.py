# Write a program to get the following output 
    #    input=‘hai hello’ 
    #    output=’olleh iah’ 

s = input("enter the string : ")
i = len(s) -1
result = ""
while i >= 0:
    result += s[i]
    i -= 1

print(result)