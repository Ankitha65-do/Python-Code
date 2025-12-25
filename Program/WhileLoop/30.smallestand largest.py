# Write a program to accept 10 numbers from the user and display the largest & smallest 
# number number. 

count = 0

n = int(input("enter the the number : "))
largest = n
smallest = n
count = 1

while count < 10:
    n = int(input("enter the number : "))
    if n > largest:
        largest = n
    if n < smallest :
        smallest = n
    
    count += 1

print("largest number is : ", largest)
print("smallest number is :", smallest)