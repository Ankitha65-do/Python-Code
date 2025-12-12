# write a program to print all even numbers that falls between two numbers (exclusive 
# both numbers) entered from the user using while loop. 

n = int(input("Enter the first number : "))
m = int(input("Enter the Last Number : "))
while n < m:
    if n % 2 == 0:
        print(n)
        n += 1
    else:
        n += 1
        print(n)
        n += 1



# Example Input/Output 1:
