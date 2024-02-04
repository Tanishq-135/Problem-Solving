n = int(input('Enter a number:'))

if n < 0:
    print('{} is a negative number, cannot be a prime number'.format(n))

elif n == 0 or n == 1:
    print('{} is neither prime nor composite number'.format(n))
    
else:
    flag = 0
    for i in range(2, n):
        if n % i == 0:
            flag = 1
            break
    
    if flag == 1:
        print('{} is not a Prime number'.format(n))
    else:
        print('{} is a Prime number'.format(n))
