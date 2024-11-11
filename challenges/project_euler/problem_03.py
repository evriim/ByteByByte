"""
Project Euler (Problem 03)
The prime factors of 13195 are 5,7,13 and 29.
What is the largest prime factor of te number 600851475143?
"""
import math

def is_prime(x):
    """Determine if a number `x` is prime."""
    if x <= 1:
        return False
    if x % 2 == 0:
        return x == 2  # 2 is the only even prime
    # Check for factors only up to the square root of `x`, skipping even numbers
    for j in range(3, int(math.sqrt(x)) + 1, 2):
        if x % j == 0:
            return False
    return True

# Define the number to find the largest prime factor for
NUMBER = 600851475143

# Start with the largest possible factor, the integer square root of `NUMBER`
i = int(math.sqrt(NUMBER))

# Loop to find the largest prime factor
while True:
    # Check if `i` divides `NUMBER` and is prime
    if NUMBER % i == 0 and is_prime(i):
        break  # Exit loop once the largest prime factor is found
    i -= 1

# Print the largest prime factor found
print(i)
