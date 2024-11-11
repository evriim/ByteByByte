"""
Project Euler (Problem 04)
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit number is 9009 =91*99.Find the largerst 
palindrome made from the product of two 3-digit numbers.
"""
# Initialize the variable to store the largest palindrome found
PAL = 0

# Loop through all pairs of 3-digit numbers
for i in range(100, 1000):
    for j in range(100, 1000):
        # Calculate the product of the two numbers
        k = i * j

        # Convert the product to a list of its digits
        list_k = [int(x) for x in str(k)]
        
        # Create the reverse of the digit list
        list_reverse = list_k[::-1]

        # Check if the product is a palindrome and is the largest found so far
        if list_k == list_reverse and k > PAL:
            PAL = k  # Update PAL if a larger palindrome is found

# Print the largest palindrome found
print(PAL)
