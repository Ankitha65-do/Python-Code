#  Write a program to check whether a number is prime or not using while loop.

n = int(input("Enter the Number : "))
i = 2
while  i < n:
    if n % i == 0:
        print(n, "is not a prime number")
        break
    i += 1
else:
    print(n, "is a prime number")


    
    