n = int(input('Enter a number:'))
fact = 1

if n < 0:
    print('{}: Cannot determine factorial of negative number'.format(n))

elif n == 0 or n == 1:
    print('Factorial of {} is 1'.format(n))

else:
    for i in range(2,n+1):
        fact *= i

    print('Factorial of {} is {}'.format(n, fact))
