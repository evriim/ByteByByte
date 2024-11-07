"""
The problem requires finding the maximum profit from buying and selling stock, given the `prices` array.
We can only buy once and sell once, and we must sell after buying.

The approach here is to:
1. Track the lowest price (`start`) seen so far.
2. Calculate the potential profit if the current price (`end`) is higher than `start`.
3. Update the maximum profit (`result`) if a higher profit is found.
"""

class Solution(object):
    def maxProfit(self, prices):
        result = 0  # Initialize result to store the maximum profit
        start = prices[0]  # Set the initial lowest price as the first price in the list
        
        # Loop through prices starting from the second element
        for end in prices[1:]:
            if end > start:
                # Calculate profit and update result if it's higher than the current result
                result = max(result, end - start)
            else:
                # Update start to the current price if it's lower than the previous start
                start = end
        
        # Return the maximum profit found
        return result
