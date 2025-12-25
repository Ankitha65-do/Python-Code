# Write a program to check whether a number is palindrome or not.

n = int(input("Enter the number : "))
num = n
palindrome = 0
while n > 0 :
    reminder = n % 10
    palindrome = palindrome * 10 + reminder
    n = n // 10

if num == palindrome:
    print("This number is Palindrome Number")
else:
    print("It's not a Palindrome Number")