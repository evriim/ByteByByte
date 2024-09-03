"""
The prime factors of 13195 are 5,7,13 and 29.
What is the largest prime factor of te number 600851475143?
"""
import math

def is_prime(x):
    """Is the number prime or not?"""
    if x % 2 == 0:
        return False
    for j in range(3,int(math.sqrt(x))+1,2):
        if x%j ==0:
            return False
    return True

NUMBER = 600851475143
i = int(math.sqrt(NUMBER))
while True:
    if NUMBER % i == 0 and is_prime(i):
        break
    i-=1

print(i)
