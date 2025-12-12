#  Write a program to print table of a number entered from the user.

n = int(input("Enter the table number to print : "))
i = 1
while i <= 10:
    print(n, "x", i, "=", n*i)
    i += 1
