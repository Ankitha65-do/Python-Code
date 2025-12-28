#  Write a python program to get the following output 
# 1—–49 
# 2—–48 
# 3—–47 
# … 
# … 
# 48—–2 
# 49—–1


start = 1
end = 49

while start <= 49 and end >= 1 :
    print(start, "---", end)
    start += 1
    end -= 1
