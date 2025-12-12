# Write a program to print the Fibonacci series till n terms (Accept n from user) using 
# while loop. 

n = int(input("Enter the Number : "))
a = 0
b = 1
fibo = 0
while fibo <= n:
    print(a, end = " ")
    c = a + b
    a = b 
    b = c
    fibo += 1