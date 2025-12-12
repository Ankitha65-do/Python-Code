#  Write a program to reverse the number accepted from user using while loop. 

n = int(input("Enter the number to be Reversed : "))
num = n
reverse = 0
while 0 < num :
    module = num % 10
    reverse = reverse * 10 + module
    num  = num // 10
print("The reversed number of", n, "is",reverse)