# Write a program to find the sum of the digits of a number accepted from the user. 

n = int(input("Enter a number: "))
sum = 0
while n > 0:
    module = n % 10
    sum += module
    n = n // 10
print(sum)

