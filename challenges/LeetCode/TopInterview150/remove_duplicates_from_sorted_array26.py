"""
The problem asks you to remove duplicates from a sorted integer array, nums, in-place.
You need to modify the array so that the first k elements contain only the unique values
from nums while preserving the order of appearance. After this, the remaining elements in
the array don't matter. Finally, you should return k, which is the number of unique elements in the array.
"""
class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        j = 0  # Pointer for the next unique element
        for i in range(1, len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
        
        return j + 1  # Length of the array with unique elements
