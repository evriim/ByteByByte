"""
2520 is the smallest number that can be divided by each of the numbers 
from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

import math
print(math.lcm(10,11,12,13,14,15,16,17,18,19,20))

"""
It can be solved faster with mathematical knowledge rather than coding.
1 = 1           11 = 11  
2 = 2           12 = (2^2)*(3)
3 = 3           13 = 13 
4 = (2^2)       14 = 2*7  
5 = 5           15 = 3*5  
6 = 2*3         16 = (2^4)
7 = 7           17 = 17
8 = (2^3)       18 = (2)*(3^2)
9 = (3^2)       19 = 19
10 = 2*5        20 = (2^2)*5

(2^4)*(3^2)*(5)*(7)*(11)*(13)*(17)*(19) = 232792560
"""
