"""
The solution is focused on keeping track of the lowest price seen so far (start) 
and calculating the potential profit if the current price (end) is higher than start.
The maximum profit is updated if a higher profit is found.
"""
class Solution(object):
    def maxProfit(self, prices):
        result= 0
        start=prices[0]
        for end in prices[1:]:
            if end > start :
                result = max(result,end-start)
            else:
                start = end
        return result
