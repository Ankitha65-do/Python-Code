# Write a python program  to sum the sequence: 
# 1 + 1/1! + 1/2! + 1/3! + …….. + 1/n!

n = int(input("Enter the NUmber : "))
sum = 1
fact = 1
i = 1
while n >= i:
    fact = fact *i
    sum = sum + 1 / fact
    i += 1

print("Sum of Sequence is :", sum)