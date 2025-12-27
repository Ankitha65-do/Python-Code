#  Write a program to print the following series till n terms. 
# 2 , 22 , 222 , 2222 _ _ _ _ _ n terms 

n = int(input("enter the number : "))
start = 2
i = 1

while n >= i:
    print(start)
    start = start * 10 + 2
    i += 1

