# Write a program to convert all the lower case charater to upper case 
# characters present in a given string 

s = str(input("enter the string : "))
i = 0
result = ""
while i < len(s):
    if not s[i].isupper():
        result += s[i].upper()
    else:
        result += s[i] 
    i += 1
print("Upper case string is :", result)