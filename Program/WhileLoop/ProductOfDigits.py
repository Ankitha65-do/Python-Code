# Q15. Write a program to find the product of the digits of a number accepted from the user. 

n = int(input("Enter the number : "))
product = 1
i = n
while 0 < i:
    modules = i % 10
    product = product * modules
    i = i //10
print("the Product of", n, "is", product)
