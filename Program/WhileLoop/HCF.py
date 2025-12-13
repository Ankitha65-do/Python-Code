# Write a program to find the HCF of two numbers entered from the user. 

a = int(input("Enter the number : "))
b = int(input("Enter the number : "))
hcf = 1
i = 1
if a > b:
    min_num = b
else : 
    min_num = a

while i <= min_num:
    if a % i == 0 and b % i == 0:
        hcf = i
    i += 1
print("HCf of ",a, "and ", b, "is", hcf) 