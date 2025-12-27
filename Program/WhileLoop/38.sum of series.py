# Write a program to find the sum of following series: 
# 1 + 2 + 6 + 24 + 120 . . . . . n terms 

n = int(input("enter the n value : "))
fact = 1
sum = 0
i = 1
while n >= i:
    fact = fact *i
    sum = sum + fact
    i += 1
print(sum)