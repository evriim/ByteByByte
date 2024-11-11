"""
2520 is the smallest number that can be divided by each of the numbers 
from 1 to 10 without any remainder. What is the smallest positive 
number that is evenly divisible by all of the numbers from 1 to 20?

Mathematical Insight:
To solve it without coding, consider the prime factorization of each 
number from 1 to 20. The LCM must include the highest powers of each 
prime factor present within this range:

- 2: The highest power in the range is \(2^4 = 16\)
- 3: The highest power is \(3^2 = 9\)
- 5: The highest power is \(5^1 = 5\)
- 7, 11, 13, 17, and 19 are primes in the range.

Thus, the smallest number divisible by all numbers from 1 to 20 is:
(2^4) * (3^2) * (5) * (7) * (11) * (13) * (17) * (19) = 232792560
"""

import math

# Calculate the LCM of numbers from 10 to 20 (since 1 to 9 are factors of these)
print(math.lcm(10,11,12,13,14,15,16,17,18,19,20))
