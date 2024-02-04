n = int(input('Enter a number:'))

if n < 0:
    print('{}: Invalid input'.format(n))

elif n == 0 or n == 1:
    print('{} is neither prime nor composite number'.format(n))
    
else:
    sum = 0
    for i in range(2, n+1): 
        flag = 0
        for j in range(2, i):
            if i % j == 0:
                flag = 1
                break
        
        if flag == 0:
            sum += i

    print('Sum =', sum)
