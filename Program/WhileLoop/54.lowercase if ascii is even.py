# Write a program to extract all the lower case character from the given 
# string only if its ascii value is even 

s = input("enter the string : ")
i = 0
result = ""
while len(s) > i:
    ch = s[i]
    if ch.islower():
        if ord(ch) % 2 == 0:
            result += ch
    i += 1
print("lowercase character with ever ASCII: ", result)

