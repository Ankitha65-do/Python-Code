# Write a program to find the sum of following series : 
# x + x2/2 + ……….xn/n

n = int(input("enter the n value : "))
x = int(input("enter the x value : "))

sum = 0
i = 1
while n >= i:
    # fact = fact * i
    sum = sum + (x ** i)/i
    i += 1
print(sum)