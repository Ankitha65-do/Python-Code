# write a program to count the number of vowels present in a given string

s = input("enter the string : ")
i = 0
count_vowels = 0
while len(s) > i:
    if s[i] in "aeiouAEIOU":
        count_vowels += 1
    i += 1
print(count_vowels)