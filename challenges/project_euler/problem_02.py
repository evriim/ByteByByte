"""
Project Euler (Problem 02)
Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
By starting with 1 and 2, the first 10 terms will be: 1,2,3,5,8,13,21,34,55,89,... By
considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
"""
# Initialize Fibonacci sequence terms and the total sum of even terms
i, j, k = 1, 1, 1
TOTAL = 0

# Generate Fibonacci terms while the term `i` is less than 4 million
while i < 4000000:
    # Calculate the next term in the sequence
    i = j + k
    
    # Update the previous two terms
    j = k
    k = i
    
    # If the term is even, add it to the total sum
    if i % 2 == 0:
        TOTAL += i

# Print the sum of even-valued terms
print(TOTAL)
