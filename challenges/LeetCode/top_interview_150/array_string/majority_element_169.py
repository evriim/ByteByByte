"""
The problem asks to find the majority element in an array, i.e., 
the element that appears more than half the time. A natural approach
is to count the frequency of each element and then return the one 
with the highest count.
"""
class Solution(object):
    def majorityElement(self, nums):
        """All inputs provided by LeetCode"""
        k={}
        for counter in range(len(nums)):
            if nums[counter] in k:
                k[nums[counter]]+=1
            else:
                k[nums[counter]]=1
        return max(k, key=k.get)
    
