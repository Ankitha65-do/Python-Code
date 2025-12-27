# Write a program to find the sum of the following series(accept values of x and n from 
# user) 
# 1 + x/1! + x2/2! + ……….xn/n!

n = int(input("enter the n value : "))
x = int(input("enter the x value : "))
fact = 1
sum = 1
i = 1 
while n >= i :
    fact = fact * i
    sum = sum + (x ** i)/fact
    i += 1
print(sum)

