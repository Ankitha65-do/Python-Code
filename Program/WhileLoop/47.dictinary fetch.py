#  Write a program to fetch only even values from a dictionary. 
# dic = {'val1':10, 'val2':20, 'val3':23, 'val4':22 } 

dic = {'val1':10, 'val2':20, 'val3':23, 'val4':22 } 
i = 0
keys = list(dic.keys())
while len(dic) > i:
    if dic[keys[i]] % 2 == 0 :
        print(dic[keys[i]])
    i += 1