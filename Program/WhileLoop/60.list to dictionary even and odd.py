# Write a program to get the following output 
    #    input=‘hai hello good morning’ 
    #    output={‘hai’:’a’ , ‘hello’: ‘l’ , ‘good’:’gd’ , ‘morning’:’n’} 

n = input("enter the string : ")
i = 0 
result = {}
words = n.split()
while len(words) > i :
    w = words[i]
    if len(w) % 2 == 0:
        result[w] = w[0] + w[-1]
    else : 
        result[w] = w[len(w) // 2]
    i += 1
print(result)