#  Write a program to print the factorial of a number accepted from user.

n = int(input("Enter the number : "))
factorial = 1
i = 1
while i <= n:
    factorial *= i
    i += 1
print(factorial)
   
   