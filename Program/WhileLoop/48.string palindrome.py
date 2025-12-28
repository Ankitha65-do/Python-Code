# Write a program to extract all the string data items from the given list only 
# if string is palindrome 

n = [121, 'madam', 'python', 'level', 45, 'noon', 'world']
i = 0
palindrome = []
while len(n) > i:
    if type(n[i]) == str:
        if n[i] == n[i][::-1]:
            palindrome.append(n[i])
    i += 1
print(palindrome)