"""
Project Euler (Problem 01)
If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3,5,6 and 9. The sum of the multiples is 23. Find the sum of all
the multiples of 3 or 5 below 1000
"""

# Initialize a variable to store the sum of multiples
TOTAL = 0

# Iterate through numbers from 0 to 999
for i in range(1000):
    # Check if `i` is a multiple of 3 or 5
    if i % 3 == 0 or i % 5 == 0:
        TOTAL += i  # Add `i` to the total if condition is met

# Print the final result
print(TOTAL)
