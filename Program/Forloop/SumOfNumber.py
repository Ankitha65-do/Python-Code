# total = 0
# for i in range(1,101):
#     sum = i +total
#     total = sum

# print(total)

# using user input to find sum of n numbers
n = int(input("enter the number: "))
total = 0
for i in range(1, n+1):
   total = total +i
print ("sum of number from ",1, "to", n," is :", total)
