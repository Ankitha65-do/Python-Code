# Write a program that appends the type of elements from a list. 
# n = [23, 'Python',23.98] 

n = [23, 'Python',23.98] 
i = 0
types = []
while len(n) > i:
    types.append(type(n[i]))
    i += 1
print(types ,end= " ")


