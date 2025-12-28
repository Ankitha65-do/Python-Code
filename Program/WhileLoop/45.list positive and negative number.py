# Write a Program to separate positive and negative number from a list. 
# x = eval(input('enter the list:')) 


x = eval(input("enter the list : "))
positive = []
negative = []
i = 0
while len(x) > i:
    if x[i] > 0:
       positive.append(x[i])
    else :
       negative.append(x[i])
    i += 1
print("positive numbers are :", positive)
print("negative numbers are  : ",negative)


