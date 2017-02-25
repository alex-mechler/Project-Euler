import math

def is_prime(n):
    for x in range(2, n):
        if n % x == 0:
            return False
    return True

div = 0
for x in range(1, int(math.sqrt(600851475143))):
    if 600851475143 % x == 0 and is_prime(x):
        div = x

print(div)