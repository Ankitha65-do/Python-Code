#  Write a program to find the sum of following series: 
# S = 1 + 4 – 9 + 16 – 25 + 36 – … … n terms

n = int(input("enter the n value : "))
sum = 0
i = 1

while i <= n :
    if i % 2 == 0:
        sum = sum - (i ** 2)
    else:
        sum = sum + (i ** 2)
    i += 1
   
print(sum)

