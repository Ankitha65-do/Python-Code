# Write a program to enter the numbers till the user enter ZERO and at the end it should 
# display the count of positive and negative numbers entered.

n = int(input("Enter the number (0 to stop) : "))
positive_count = 0
negative_count = 0

while n != 0:
    if n > 0:
        positive_count += 1
    else: 
        negative_count += 1
    n = int(input("Enter the number (0 to stop) : "))
print("Positive Number are :",positive_count)
print("Negative Number are :", negative_count)