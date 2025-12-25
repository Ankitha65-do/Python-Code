# Write a program to accept 10 numbers from the user and display it’s average

count = 0
total = 0

while count < 10:
    n = int (input("enter the number : "))
    total += n
    count += 1
avg = total /10
print("Average is :", avg)