arr1 = [1,2,3,4,5]
arr2 = [5,7,9,1,2,3]
union = []
inter = []

if len(arr1) > len(arr2):
    for i in arr2:
        if i in arr1:
            inter.append(i)
    
    union = arr1
    for i in arr2:
        if i not in union:
            union.append(i)
            
else:
    for i in arr1:
        if i in arr2:
            inter.append(i)
            
    union = arr2
    for i in arr1:
        if i not in union:
            union.append(i)

#union = list(set(arr1+arr2)) #Python Specific

print('Union:',sorted(union))
print('Intersection:',sorted(inter))
