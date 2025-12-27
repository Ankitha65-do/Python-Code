# Write a program to print the following series till n terms. 
# 1 4 9 16 25 _ _ _ _ _ n terms. 

n = int(input("Enter the number : " ))
i = 1
while n >= i:
    print( i*i)
    i += 1