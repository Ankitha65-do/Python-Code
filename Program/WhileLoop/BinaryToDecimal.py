# . Write a program to convert Binary to Decimal.

n = str(input("Enter the Number : "))
num = n
decimal_num = 0
power = 0

while  n > "0" :
    last_digit = int(n[-1])
    decimal_num = decimal_num + last_digit * (2 ** power)
    n = n[:-1]
    power = power + 1

print("Decimal Number of ", num, "is : ", decimal_num)

