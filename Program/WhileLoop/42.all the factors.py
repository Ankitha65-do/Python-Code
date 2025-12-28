# Write a program to print all the factors of a number using while loop. 

n = int(input("enter the n value : "))
i = 1
while n >= i:
    if n % i == 0:
        print(i)
    i += 1
