# Write a program to convert Decimal to Binary.

n = int(input("enter the number : "))
num = n
i = 2
binary_num = ""
while n > 0 :
    reminder = n % i 
    binary_num = str(reminder) + binary_num 
    n = n // i

print("Binary Number of ", num , "is", binary_num)
    