"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10001st prime number?
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

COUNTER=2
NUMBER=4
while COUNTER != 10001:
    NUMBER+=1
    if is_prime(NUMBER):
        COUNTER+=1

print(NUMBER)
