# Write a program to convert all the lower case character to upper case 
# character and upper case character to lower  case character by keeping number 
# and special character as it is 

s = input("enter the string: ")
i = 0
result = ""
while len(s) > i :
    if not s[i].isupper():
        result += s[i].upper()
    elif not s[i].islower() :
        result += s[i].lower()
    elif s[i].isdigit() :
        result += s[i].digit()
    else:
        result += s[i].special()
    i += 1
print("output is : ", result)