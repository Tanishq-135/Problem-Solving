# All digits, 153, 370, 371, 407, 1634, 8208
n = int(input('Enter a number:'))
num = n
sum = 0
length = len(str(n))


if n <= 0:
    print('{} cannot be an Armstrong number')

else:
    while num > 0:
        rem = num % 10
        sum += rem ** length
        num //= 10
    
    if n == sum:
        print('{} is an Armstrong number'.format(n))
    else:
        print('{} is not an Armstring number'.format(n))
