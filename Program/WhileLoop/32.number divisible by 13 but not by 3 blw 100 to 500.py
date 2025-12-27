#  Write a program to display all the numbers which are divisible by 13 but not by 3 
# between 100 and 500.(exclusive both numbers) 

start = 100
end = 500
num = start + 1
while num < end:
    if num % 13 == 0 and num % 3 != 0 :
        print(num)
    num += 1
