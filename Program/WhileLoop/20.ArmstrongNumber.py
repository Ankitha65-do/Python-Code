# Write a program to check whether a number is Armstrong or not. (Armstrong number is 
# a number that is equal to the sum of cubes of its digits for example : 153 = 1^3 + 5^3 + 3^3.)

n = int(input("Enter the number : "))
num = n
armstrong = 0

while 0 < num:
    modules = num % 10
    armstrong += modules * modules * modules
    num = num //10

if armstrong == n:
    print(n, "It's a armstrong number")
else:
    print(n, "It's not a armstrong number")

