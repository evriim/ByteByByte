"""
The problem requires finding the majority element in an array, 
which is defined as the element that appears more than half the time.

A straightforward approach is to use a dictionary to count the frequency 
of each element, then return the element with the highest count.
"""

class Solution(object):
    def majorityElement(self, nums):
        """All inputs provided by LeetCode"""
        k = {}  # Initialize an empty dictionary to store element frequencies
        
        # Iterate through each element in the array
        for counter in range(len(nums)):
            if nums[counter] in k:
                k[nums[counter]] += 1  # Increment count if element is already in dictionary
            else:
                k[nums[counter]] = 1  # Add new element with count 1 if it's not in dictionary
        
        # Find the key with the maximum value (frequency) in the dictionary
        return max(k, key=k.get)
