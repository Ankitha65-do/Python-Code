# write a program to print all even numbers that falls between two numbers (exclusive 
# both numbers) entered from the user using while loop. 

n = int(input("Enter the first number : "))
m = int(input("Enter the Last Number : "))
i = n + 1
while i < m:
    if i % 2 == 0:
        print(i)
    i += 1
    



# Example Input/Output 1:
