# Write a program to add first n terms of the following series using a while loop: 
# 1/1! + 1/2! + 1/3! + …….. + 1/n!

n = int(input("Enter the number : "))
fact = 1
sum = 0
i = 1

while i < n:
    fact *= i
    sum += 1/fact
    i += 1
print("sum of series is : ", sum)
