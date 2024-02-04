str1 = 'Tanishq'
str2 = ''
char = '@'

for i in str1:
    ch = i
    str2 = ch + str2

str1 = ''

for i in str2:
    if str2.index(i) == len(str2) - 1:
        str1 = str1 + i
    else:
        str1 = str1 + i + char

print(str1)
