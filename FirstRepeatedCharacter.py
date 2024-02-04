str = "abcbacc"
n = len(str)
index = 99999999
	
for i in range(n):
	for j in range(i+1, n):
		if str[j] == str[i]:
			if j < index:
				index = j
				ans = str[j]
	
print('First repeating character:', ans) 
