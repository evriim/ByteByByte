"""
Project Euler (Problem 06)
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385 The square of the sum of the 
first ten natural numbers is, (1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the 
first ten natural numbers and the square of the sum is 3025 - 385 = 2640
Find the difference between the sum of the squares of the first 
one hundred natural numbers and the square of the sum.
"""
import math

# Initialize variables to store the sum of squares and the square of the sum
SUM_OF_SQUARES = 0
SQUARE_OF_SUM = 0

# Calculate the sum of squares
for i in range(1, 101):
    SUM_OF_SQUARES += math.pow(i, 2)

# Calculate the sum of numbers and then square it
for j in range(1, 101):
    SQUARE_OF_SUM += j

# Find the difference by subtracting the sum of squares from the square of the sum
result = int(math.pow(SQUARE_OF_SUM, 2) - SUM_OF_SQUARES)
print(result)
