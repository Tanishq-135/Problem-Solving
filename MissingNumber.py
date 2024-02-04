arr = [0,1,2,3,4,6,7,8,9]
n = len(arr)

for i in range(0, n):
    if i not in arr:
        print(i)
        break
else:
    print('Every number is present inside the list within range')
