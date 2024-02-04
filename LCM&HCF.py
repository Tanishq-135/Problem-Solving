n1 = int(input('Enter first number:'))
n2 = int(input('Enter second number:'))

if n1 > n2:
    max, min = n1, n2
else:
    max, min = n2, n1

prod = n1 * n2

while prod % max == 0 and prod % min == 0:
    lcm = prod
    prod //= min

prod = n1 * n2

hcf = prod // lcm

print('HCF:', hcf)
print('LCM:', lcm)
