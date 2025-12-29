# .Write a program to get the following output 
#    input=[‘hai’ , 89 ,3.4 , ‘hello’ , 90 , ‘py’] 
#    output={‘hai’:’hi’ , ‘hello’:’ho’ , ‘py’:’py’}

s =  eval(input("enter the list : "))
i = 0 
result = {}
while len(s) > i :
    if type(s[i]) == str:
        result[s[i]] = s[i][0] + s[i][-1]
    i += 1
print(result)
        
        
    

 
      