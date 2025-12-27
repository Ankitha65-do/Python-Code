# Write a program to find the sum of following series 
# 1 + 8 + 27 …………n terms

n = int(input("enter the number : "))
i = 1
sum = 0
while n >= i:
    sum = sum + (i ** 3)
    i += 1
print(sum)
