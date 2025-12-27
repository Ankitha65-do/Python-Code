# . Write a program to display sum of odd numbers and even numbers separately that fall 
# between two numbers accepted from the user.(including both numbers) using while loop.

n = int(input("enter the start number : "))
m = int(input("enter the end number : "))
even_sum = 0
odd_sum = 0
num = n
while num <= m :
    if num % 2 == 0:
        even_sum = even_sum + num
    else :
        odd_sum = odd_sum + num
    num += 1
print("Even number sum is : ", even_sum)
print("Odd number sum is : ", odd_sum)